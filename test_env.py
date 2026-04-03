from env import TravelEnv

env = TravelEnv()

state = env.reset()
print("Initial State:", state)

for i in range(5):
    action = 0  # try same action
    state, reward, done, _ = env.step(action)
    
    print(f"Step {i+1}:")
    print("State:", state)
    print("Reward:", reward)
    print("Done:", done)
    
    if done:
        break