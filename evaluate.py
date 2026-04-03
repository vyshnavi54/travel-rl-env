from env import TravelEnv

# 🟢 Easy Task
def easy_task():
    env = TravelEnv()
    state = env.reset()
    
    total_reward = 0
    
    for _ in range(3):
        action = 2  # always choose Park (cheap + nature)
        state, reward, done, _ = env.step(action)
        total_reward += reward
        
        if done:
            break

    # Normalize score (0 to 1)
    score = max(0, min(1, total_reward / 20))
    return score


# 🟡 Medium Task
def medium_task():
    env = TravelEnv()
    state = env.reset()
    
    total_reward = 0

    for _ in range(3):
        # simple logic: choose based on budget
        if state["budget"] > 2000:
            action = 0  # Beach
        else:
            action = 2  # Park
        
        state, reward, done, _ = env.step(action)
        total_reward += reward
        
        if done:
            break

    score = max(0, min(1, total_reward / 20))
    return score


# 🔴 Hard Task
def hard_task():
    env = TravelEnv()
    state = env.reset()
    
    total_reward = 0

    for _ in range(3):
        # smarter logic: match preference + budget
        if "nature" in state["preferences"] and state["budget"] >= 3000:
            action = 0  # Beach
        elif state["budget"] >= 1000:
            action = 2  # Park
        else:
            action = 1  # Temple
        
        state, reward, done, _ = env.step(action)
        total_reward += reward
        
        if done:
            break

    score = max(0, min(1, total_reward / 20))
    return score


# Run all tasks
if __name__ == "__main__":
    print("Easy Task Score:", easy_task())
    print("Medium Task Score:", medium_task())
    print("Hard Task Score:", hard_task())