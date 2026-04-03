import random

class TravelEnv:
    def __init__(self):
        self.current_state = None
        self.done = False

    def reset(self):
        self.current_state = {
            "budget": random.choice([3000, 5000, 7000]),
            "preferences": random.choice([
                ["nature"], 
                ["spiritual"], 
                ["nature", "spiritual"]
            ]),
            "day": 1
        }
        self.done = False
        return self.current_state

    def state(self):
        return self.current_state

    def step(self, action):
        place_info = {
            0: {"name": "Goa Beach", "cost": 4000, "type": "nature", "rating": 4.5},
            1: {"name": "Tirupati Temple", "cost": 2000, "type": "spiritual", "rating": 5.0},
            2: {"name": "City Park", "cost": 1000, "type": "nature", "rating": 3.5}
        }

        reward = 0
        chosen_place = place_info[action]

        # ✅ Use updated preferences from state
        preferences = self.current_state["preferences"]

        # 1. Preference match
        if chosen_place["type"] in preferences:
            reward += 5
            user_click = True
        else:
            reward -= 2
            user_click = False

        # 2. Budget handling
        if chosen_place["cost"] <= self.current_state["budget"]:
            reward += 3
            self.current_state["budget"] -= chosen_place["cost"]
        else:
            reward -= 5

        # 3. Rating
        reward += chosen_place["rating"]

        # 4. User satisfaction
        if user_click:
            reward += 2
        else:
            reward -= 1

        # Update state
        self.current_state["day"] += 1

        # End condition
        if self.current_state["day"] > 3:
            self.done = True

        return self.current_state, reward, self.done, {}
