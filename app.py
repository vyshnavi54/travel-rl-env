from flask import Flask, request, jsonify
from env import TravelEnv

app = Flask(__name__)

env = TravelEnv()

@app.route("/reset", methods=["POST"])
def reset():
    state = env.reset()
    return jsonify(state)

@app.route("/step", methods=["POST"])
def step():
    data = request.get_json()
    action = data.get("action")

    state, reward, done, _ = env.step(action)

    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })

@app.route("/state", methods=["GET"])
def state():
    return jsonify(env.state())

@app.route("/")
def home():
    return "Travel RL Environment Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
