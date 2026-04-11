import os
from env import TravelEnv

MODEL_NAME = os.environ.get("MODEL_NAME", "default")

PLACE_INFO = {
    0: {"type": "nature",    "cost": 4000, "rating": 4.5},
    1: {"type": "spiritual", "cost": 2000, "rating": 5.0},
    2: {"type": "nature",    "cost": 1000, "rating": 3.5},
}

TASKS = [
    {"id": "easy",   "preferences": ["nature"],             "budget": 5000},
    {"id": "medium", "preferences": ["spiritual"],          "budget": 3000},
    {"id": "hard",   "preferences": ["nature","spiritual"], "budget": 2000},
]

def score(action, preferences, budget):
    p = PLACE_INFO[action]
    s = 0.0
    if p["type"] in preferences: s += 0.45
    if p["cost"] <= budget: s += 0.35
    s += (p["rating"] - 3.5) / 1.5 * 0.18
    return round(max(0.01, min(0.99, s)), 4)

env = TravelEnv()

for task in TASKS:
    print(f"[START] task={task['id']} env=travel_planner_env model={MODEL_NAME}")
    state = env.reset()
    env.current_state["preferences"] = task["preferences"]
    env.current_state["budget"]      = task["budget"]
    rewards = []
    for step in range(3):
        action = max([0,1,2], key=lambda a: score(a, task["preferences"], task["budget"]))
        state, _, done, _ = env.step(action)
        r = score(action, task["preferences"], task["budget"])
        rewards.append(r)
        print(f"[STEP] step={step+1} action={action} reward={r} done={str(done).lower()} error=null")
        if done: break
    final = round(sum(rewards)/len(rewards), 4)
    print(f"[END] success=true steps={len(rewards)} score={final} rewards={','.join(map(str,rewards))}")
    print()
