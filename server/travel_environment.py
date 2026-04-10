import random
from uuid import uuid4
from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import TravelAction, TravelObservation

PLACE_INFO = {
    0: {"name": "Goa Beach",       "cost": 4000, "type": "nature",    "rating": 4.5},
    1: {"name": "Tirupati Temple", "cost": 2000, "type": "spiritual", "rating": 5.0},
    2: {"name": "City Park",       "cost": 1000, "type": "nature",    "rating": 3.5},
}

def _compute_reward(action: int, budget: int, preferences: list) -> float:
    """Returns reward strictly between 0 and 1."""
    place = PLACE_INFO.get(action, PLACE_INFO[2])
    score = 0.0
    # preference match: 0.4 weight
    if place["type"] in preferences:
        score += 0.4
    # budget fit: 0.35 weight
    if place["cost"] <= budget:
        ratio = 1.0 - (place["cost"] / max(budget, 1)) * 0.5
        score += 0.35 * ratio
    else:
        score += 0.05
    # rating: 0.25 weight, rating is 3.5–5.0 → map to 0–1
    score += 0.25 * (place["rating"] - 3.5) / 1.5
    return round(max(0.01, min(0.99, score)), 4)


class TravelEnvironment(Environment):
    def __init__(self):
        self._budget = 5000
        self._preferences = ["nature"]
        self._day = 1
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self._done = False

    def reset(self) -> TravelObservation:
        self._budget = random.choice([3000, 5000, 7000])
        self._preferences = random.choice([["nature"], ["spiritual"], ["nature", "spiritual"]])
        self._day = 1
        self._done = False
        self._state = State(episode_id=str(uuid4()), step_count=0)
        return TravelObservation(
            budget=self._budget,
            preferences=self._preferences,
            day=self._day,
            place_visited="",
            done=False,
            reward=0.5,   # initial reward must also be in (0,1)
        )

    def step(self, action: TravelAction) -> TravelObservation:
        self._state.step_count += 1
        a = action.action
        place = PLACE_INFO.get(a, PLACE_INFO[2])

        if place["cost"] <= self._budget:
            self._budget -= place["cost"]

        self._day += 1
        done = self._day > 3

        reward = _compute_reward(a, self._budget, self._preferences)

        return TravelObservation(
            budget=self._budget,
            preferences=self._preferences,
            day=self._day,
            place_visited=place["name"],
            done=done,
            reward=reward,
        )

    @property
    def state(self) -> State:
        return self._state