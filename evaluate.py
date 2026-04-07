from env import TravelEnv
import random

# Normalize score strictly between (0,1)
def normalize(value):
    value = value / 100
    if value <= 0:
        return 0.1
    if value >= 1:
        return 0.9
    return value


# REQUIRED: grader functions must start with "grade_"

def grade_easy():
    env = TravelEnv()
    env.reset()
    total = 0

    action = random.choice([0, 1, 2])
    _, reward, _, _ = env.step(action)
    total += reward

    return normalize(total)


def grade_medium():
    env = TravelEnv()
    env.reset()
    total = 0

    for _ in range(2):
        action = random.choice([0, 1, 2])
        _, reward, done, _ = env.step(action)
        total += reward
        if done:
            break

    return normalize(total)


def grade_hard():
    env = TravelEnv()
    env.reset()
    total = 0

    for _ in range(3):
        action = random.choice([0, 1, 2])
        _, reward, done, _ = env.step(action)
        total += reward
        if done:
            break

    return normalize(total)


# REQUIRED: explicit dictionary of graders

GRADERS = {
    "easy": grade_easy,
    "medium": grade_medium,
    "hard": grade_hard
}


if __name__ == "__main__":
    results = {}

    for name, func in GRADERS.items():
        results[name] = func()

    print(results)
