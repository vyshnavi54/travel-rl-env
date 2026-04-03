import random
from env import TravelEnv

env = TravelEnv()

print("[START] Running Travel RL Environment")

state = env.reset()
print(f"[STEP] Initial State: {state}")

total_reward = 0

for step in range(3):
    action = random.choice([0, 1, 2])
    state, reward, done, _ = env.step(action)
    
    total_reward += reward
    
    print(f"[STEP] Step {step+1}")
    print(f"[STEP] Action: {action}")
    print(f"[STEP] State: {state}")
    print(f"[STEP] Reward: {reward}")
    
    if done:
        break

print(f"[END] Total Reward: {total_reward}")