from env import TravelEnv
import random

def clamp(score):
    # strictly between (0,1)
    if score <= 0:
        return 0.01
    if score >= 1:
        return 0.99
    return score

# ✅ EASY TASK
def easy_task():
    env = TravelEnv()
    state = env.reset()

    action = random.choice([0, 1, 2])
    _, reward, _, _ = env.step(action)

    score = reward / 20
    return clamp(score)

# ✅ MEDIUM TASK
def medium_task():
    env = TravelEnv()
    state = env.reset()
    total_reward = 0

    for _ in range(2):
        action = random.choice([0, 1, 2])
        _, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    score = total_reward / 30
    return clamp(score)

# ✅ HARD TASK
def hard_task():
    env = TravelEnv()
    state = env.reset()
    total_reward = 0

    for _ in range(3):
        action = random.choice([0, 1, 2])
        _, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    score = total_reward / 50
    return clamp(score)

# ✅ RUN ALL TASKS
if __name__ == "__main__":
    easy = easy_task()
    medium = medium_task()
    hard = hard_task()

    print(f"Easy Task Score: {easy}")
    print(f"Medium Task Score: {medium}")
    print(f"Hard Task Score: {hard}")
