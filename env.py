import random

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
        chosen     = place_info[action]
        prefs      = self.current_state["preferences"]
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

        normalized = round(max(0.01, min(0.99, (reward + 10) / 25)), 4)
        return self.current_state, normalized, self.done, {}
