from env import TravelEnv
import random

def run_episode(steps):
    env = TravelEnv()
    env.reset()
    total_reward = 0

    for _ in range(steps):
        action = random.choice([0, 1, 2])
        _, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    # normalize strictly between (0,1)
    score = total_reward / 100
    if score <= 0:
        score = 0.1
    if score >= 1:
        score = 0.9

    return score


if __name__ == "__main__":
    results = {
        "easy": run_episode(1),
        "medium": run_episode(2),
        "hard": run_episode(3)
    }

    print(results)
