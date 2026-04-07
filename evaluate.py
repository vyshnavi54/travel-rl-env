from env import TravelEnv
import random

def normalize(score):
    score = score / 100
    if score <= 0:
        return 0.1
    if score >= 1:
        return 0.9
    return score


def run_env(steps):
    env = TravelEnv()
    env.reset()
    total = 0

    for _ in range(steps):
        action = random.choice([0, 1, 2])
        _, reward, done, _ = env.step(action)
        total += reward
        if done:
            break

    return normalize(total)


# ✅ REQUIRED FUNCTION (VERY IMPORTANT)
def get_tasks():
    return [
        {
            "name": "easy",
            "grader": lambda: run_env(1)
        },
        {
            "name": "medium",
            "grader": lambda: run_env(2)
        },
        {
            "name": "hard",
            "grader": lambda: run_env(3)
        }
    ]


# Optional run
if __name__ == "__main__":
    results = {}
    for task in get_tasks():
        results[task["name"]] = task["grader"]()

    print(results)
