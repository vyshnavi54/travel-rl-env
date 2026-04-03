import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify
from env import TravelEnv

app = Flask(__name__)
env = TravelEnv()

@app.route("/reset", methods=["POST"])
def reset():
    return jsonify(env.reset())

@app.route("/step", methods=["POST"])
def step():
    data = request.get_json()
    action = data.get("action")
    state, reward, done, _ = env.step(action)
    return jsonify({"state": state, "reward": reward, "done": done})

@app.route("/state", methods=["GET"])
def state():
    return jsonify(env.state())

@app.route("/")
def home():
    return "Travel RL Environment Running"

# ✅ REQUIRED main function
def main():
    app.run(host="0.0.0.0", port=7860)

# ✅ REQUIRED entry point
if __name__ == "__main__":
    main()
