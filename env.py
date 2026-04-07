import random

# ── 3 Grader functions (scores strictly between 0 and 1) ──

def grade_preference_match(action: int, state: dict) -> float:
    place_types   = {0: "nature", 1: "spiritual", 2: "nature"}
    place_ratings = {0: 4.5,     1: 5.0,         2: 3.5}
    if action not in place_types:
        return 0.01
    if place_types[action] in state.get("preferences", []):
        rating = place_ratings[action]
        score  = 0.6 + (rating - 3.5) / (5.0 - 3.5) * 0.39
    else:
        score = 0.01
    return round(max(0.01, min(0.99, score)), 4)

def grade_budget_efficiency(action: int, state: dict) -> float:
    place_costs = {0: 4000, 1: 2000, 2: 1000}
    if action not in place_costs:
        return 0.01
    budget = state.get("budget", 1) or 1
    ratio  = place_costs[action] / budget
    if ratio > 1.0:
        score = max(0.01, 0.3 - (ratio - 1.0) * 0.3)
    else:
        score = 0.5 + min(ratio, 0.9) * 0.49 / 0.9
    return round(max(0.01, min(0.99, score)), 4)

def grade_itinerary_diversity(actions_history: list) -> float:
    place_types = {0: "nature", 1: "spiritual", 2: "nature"}
    if not actions_history:
        return 0.01
    visited = set(place_types[a] for a in actions_history if a in place_types)
    score   = len(visited) / 2 * 0.98
    return round(max(0.01, min(0.99, score)), 4)


# ── Environment ────────────────────────────────────────────

class TravelEnv:
    def __init__(self):
        self.current_state   = None
        self.done            = False
        self.actions_history = []

    def reset(self):
        self.current_state = {
            "budget":      random.choice([3000, 5000, 7000]),
            "preferences": random.choice([
                ["nature"],
                ["spiritual"],
                ["nature", "spiritual"]
            ]),
            "day": 1
        }
        self.done            = False
        self.actions_history = []
        return self.current_state

    def state(self):
        return self.current_state

    def step(self, action):
        place_info = {
            0: {"name": "Goa Beach",       "cost": 4000, "type": "nature",    "rating": 4.5},
            1: {"name": "Tirupati Temple", "cost": 2000, "type": "spiritual", "rating": 5.0},
            2: {"name": "City Park",       "cost": 1000, "type": "nature",    "rating": 3.5},
        }
        chosen    = place_info[action]
        prefs     = self.current_state["preferences"]
        self.actions_history.append(action)

        reward     = 0
        user_click = chosen["type"] in prefs
        reward    += 5 if user_click else -2
        if chosen["cost"] <= self.current_state["budget"]:
            reward += 3
            self.current_state["budget"] -= chosen["cost"]
        else:
            reward -= 5
        reward += chosen["rating"]
        reward += 2 if user_click else -1

        self.current_state["day"] += 1
        if self.current_state["day"] > 3:
            self.done = True

        scores = {
            "preference_match":    grade_preference_match(action, self.current_state),
            "budget_efficiency":   grade_budget_efficiency(action, self.current_state),
            "itinerary_diversity": grade_itinerary_diversity(self.actions_history),
        }
        return self.current_state, reward, self.done, {"scores": scores, "place": chosen["name"]}
