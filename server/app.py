from flask import Flask, request, jsonify
from env import TravelEnv

app = Flask(__name__)
env = TravelEnv()

@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({"observation": env.reset()})

@app.route("/step", methods=["POST"])
def step():
    action = int(request.get_json()["action"])
    state, reward, done, info = env.step(action)
    return jsonify({"observation": state, "reward": reward, "done": done, "info": info})

@app.get("/state")
def state():
    return jsonify({"state": env.state()})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

def main():
    app.run(host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
