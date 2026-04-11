import random
from uuid import uuid4

try:
    from openenv.core.env_server.interfaces import Environment
    from openenv.core.env_server.types import State
except ImportError:
    from openenv.core.env_server.interfaces import Environment
    from openenv.core.env_server.types import State

try:
    from ..models import TravelAction, TravelObservation
except ImportError:
    from models import TravelAction, TravelObservation

PLACE_INFO = {
    0: {"name": "Goa Beach",       "cost": 4000, "type": "nature",    "rating": 4.5},
    1: {"name": "Tirupati Temple", "cost": 2000, "type": "spiritual", "rating": 5.0},
    2: {"name": "City Park",       "cost": 1000, "type": "nature",    "rating": 3.5},
}

TASKS = {
    "easy":   {"id": "easy",   "description": "Pick a place matching preferences",         "max_steps": 1},
    "medium": {"id": "medium", "description": "Stay within budget over 2 steps",           "max_steps": 2},
    "hard":   {"id": "hard",   "description": "Maximise diversity over 3 steps",           "max_steps": 3},
}

def _clamp(score: float) -> float:
    """Always return strictly between 0 and 1."""
    return round(max(0.01, min(0.99, float(score))), 4)

def grade_easy(action: int, state: dict) -> float:
    place = PLACE_INFO.get(action, PLACE_INFO[2])
    prefs = state.get("preferences", [])
    return _clamp(0.85 if place["type"] in prefs else 0.15)

def grade_medium(action: int, state: dict) -> float:
    place = PLACE_INFO.get(action, PLACE_INFO[2])
    budget = state.get("budget", 1) or 1
    ratio = place["cost"] / budget
    score = 0.85 if ratio <= 1.0 else max(0.01, 0.5 - (ratio - 1.0))
    return _clamp(score)

def grade_hard(actions_history: list) -> float:
    types = {PLACE_INFO[a]["type"] for a in actions_history if a in PLACE_INFO}
    return _clamp(len(types) / 2 * 0.97)

GRADERS = {
    "easy":   grade_easy,
    "medium": grade_medium,
    "hard":   grade_hard,
}

class TravelEnvironment(Environment):
    def __init__(self):
        self._budget = 5000
        self._preferences = ["nature"]
        self._day = 1
        self._task_id = "easy"
        self._actions_history = []
        self._state = State(episode_id=str(uuid4()), step_count=0)

    def reset(self, task_id: str = "easy") -> TravelObservation:
        self._budget = random.choice([3000, 5000, 7000])
        self._preferences = random.choice([["nature"], ["spiritual"], ["nature", "spiritual"]])
        self._day = 1
        self._task_id = task_id if task_id in TASKS else "easy"
        self._actions_history = []
        self._state = State(episode_id=str(uuid4()), step_count=0)
        return TravelObservation(
            budget=self._budget,
            preferences=self._preferences,
            day=self._day,
            place_visited="",
            task_id=self._task_id,
            done=False,
            reward=0.5,
        )

    def step(self, action: TravelAction) -> TravelObservation:
        self._state.step_count += 1
        a = action.action
        place = PLACE_INFO.get(a, PLACE_INFO[2])
        self._actions_history.append(a)

        if place["cost"] <= self._budget:
            self._budget -= place["cost"]

        self._day += 1
        max_steps = TASKS[self._task_id]["max_steps"]
        done = self._day > max_steps + 1

        # reward strictly between 0 and 1
        if self._task_id == "easy":
            reward = grade_easy(a, {"preferences": self._preferences})
        elif self._task_id == "medium":
            reward = grade_medium(a, {"budget": self._budget + place["cost"]})
        else:
            reward = grade_hard(self._actions_history)

        return TravelObservation(
            budget=self._budget,
            preferences=self._preferences,
            day=self._day,
            place_visited=place["name"],
            task_id=self._task_id,
            done=done,
            reward=reward,
        )

    @property
    def state(self) -> State:
        return self._state
