class EasyGrader:
    def grade(self, env, *args, **kwargs) -> float:
        try:
            place_info = {
                0: {"type": "nature",    "cost": 4000, "rating": 4.5},
                1: {"type": "spiritual", "cost": 2000, "rating": 5.0},
                2: {"type": "nature",    "cost": 1000, "rating": 3.5},
            }
            state = env.state() if env else {}
            budget = state.get("budget", 5000)
            preferences = state.get("preferences", ["nature"])
            best_score = 0.0
            for place in place_info.values():
                s = 0.0
                if place["type"] in preferences:
                    s += 0.45
                if place["cost"] <= budget:
                    s += 0.35
                s += (place["rating"] - 3.5) / 1.5 * 0.18
                best_score = max(best_score, s)
            return max(0.01, min(0.99, round(best_score, 4)))
        except Exception:
            return 0.5


class MediumGrader:
    def grade(self, env, *args, **kwargs) -> float:
        try:
            place_info = {
                0: {"type": "nature",    "cost": 4000, "rating": 4.5},
                1: {"type": "spiritual", "cost": 2000, "rating": 5.0},
                2: {"type": "nature",    "cost": 1000, "rating": 3.5},
            }
            state = env.state() if env else {}
            budget = state.get("budget", 3000)
            preferences = state.get("preferences", ["spiritual"])
            best_score = 0.0
            for place in place_info.values():
                s = 0.0
                if place["type"] in preferences:
                    s += 0.45
                if place["cost"] <= budget:
                    s += 0.35
                s += (place["rating"] - 3.5) / 1.5 * 0.18
                best_score = max(best_score, s)
            return max(0.01, min(0.99, round(best_score, 4)))
        except Exception:
            return 0.5


class HardGrader:
    def grade(self, env, *args, **kwargs) -> float:
        try:
            place_info = {
                0: {"type": "nature",    "cost": 4000, "rating": 4.5},
                1: {"type": "spiritual", "cost": 2000, "rating": 5.0},
                2: {"type": "nature",    "cost": 1000, "rating": 3.5},
            }
            state = env.state() if env else {}
            budget = state.get("budget", 2000)
            preferences = state.get("preferences", ["nature", "spiritual"])
            best_score = 0.0
            for place in place_info.values():
                s = 0.0
                if place["type"] in preferences:
                    s += 0.45
                if place["cost"] <= budget:
                    s += 0.35
                s += (place["rating"] - 3.5) / 1.5 * 0.18
                best_score = max(best_score, s)
            return max(0.01, min(0.99, round(best_score, 4)))
        except Exception:
            return 0.5