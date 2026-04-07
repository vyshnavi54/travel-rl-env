from env import TravelEnv
import random

def normalize(score):
    # Convert to range (0,1)
    return max(0.01, min(0.99, score / 20))

def run_task(steps):
    env = TravelEnv()
    state = env.reset()
    total_reward = 0

    for _ in range(steps):
        action = random.choice([0, 1, 2])
        state, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    return normalize(total_reward)

# ✅ 3 tasks
easy_score = run_task(1)
medium_score = run_task(2)
hard_score = run_task(3)

print("Easy Task Score:", easy_score)
print("Medium Task Score:", medium_score)
print("Hard Task Score:", hard_score)
