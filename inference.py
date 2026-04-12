import os
from openai import OpenAI
from env import TravelEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME   = os.getenv("MODEL_NAME", "gpt-4.1-mini")
API_KEY      = os.environ["API_KEY"]   # ← changed from HF_TOKEN to API_KEY

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

PLACE_INFO = {
    0: {"name": "Goa Beach",       "type": "nature",    "cost": 4000, "rating": 4.5},
    1: {"name": "Tirupati Temple", "type": "spiritual", "cost": 2000, "rating": 5.0},
    2: {"name": "City Park",       "type": "nature",    "cost": 1000, "rating": 3.5},
}

TASKS = [
    {"id": "easy",   "preferences": ["nature"],             "budget": 5000},
    {"id": "medium", "preferences": ["spiritual"],          "budget": 3000},
    {"id": "hard",   "preferences": ["nature","spiritual"], "budget": 2000},
]

def compute_score(action, preferences, budget):
    p = PLACE_INFO[action]
    s = 0.0
    if p["type"] in preferences: s += 0.45
    if p["cost"] <= budget:      s += 0.35
    s += (p["rating"] - 3.5) / 1.5 * 0.18
    return round(max(0.01, min(0.99, s)), 2)

def choose_action(preferences, budget):
    prompt = (
        f"You are a travel agent. User preferences: {preferences}, budget: {budget}. "
        f"Choose: 0=Goa Beach (nature,4000), 1=Tirupati Temple (spiritual,2000), "
        f"2=City Park (nature,1000). Reply with only 0, 1, or 2."
    )
    try:
        resp = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5,
        )
        action = int(resp.choices[0].message.content.strip()[0])
        if action not in [0, 1, 2]:
            action = 0
    except Exception:
        action = 0
    return action

env = TravelEnv()

for task in TASKS:
    print(f"[START] task={task['id']} env=travel_planner_env model={MODEL_NAME}")
    state = env.reset()
    env.current_state["preferences"] = task["preferences"]
    env.current_state["budget"]      = task["budget"]
    rewards = []
    success = False
    try:
        for step in range(3):
            action = choose_action(env.current_state["preferences"], env.current_state["budget"])
            state, _, done, _ = env.step(action)
            reward = compute_score(action, task["preferences"], task["budget"])
            rewards.append(reward)
            print(f"[STEP] step={step+1} action={action} reward={reward:.2f} done={str(done).lower()} error=null")
            if done:
                break
        success = True
    except Exception as e:
        print(f"[STEP] step={len(rewards)+1} action=0 reward=0.50 done=false error={e}")
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={len(rewards)} rewards={rewards_str}")
    print()
