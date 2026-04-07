import os
from openai import OpenAI
from env import TravelEnv

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

env = TravelEnv()

print("[START] Running Travel RL Environment")

state = env.reset()
print(f"[STEP] Initial State: {state}")

total_reward = 0

for step in range(3):

    prompt = f"State: {state}. Choose best action: 0 Beach, 1 Temple, 2 Park. Return only number."

    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
        messages=[{"role": "user", "content": prompt}]
    )

    action_text = response.choices[0].message.content.strip()

    if action_text not in ["0", "1", "2"]:
        action = 0
    else:
        action = int(action_text)

    state, reward, done, _ = env.step(action)

    total_reward += reward

    print(f"[STEP] Step {step+1}")
    print(f"[STEP] Action: {action}")
    print(f"[STEP] State: {state}")
    print(f"[STEP] Reward: {reward}")

    if done:
        break

print(f"[END] Total Reward: {total_reward}")
