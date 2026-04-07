import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from env import TravelEnv, grade_preference_match, grade_budget_efficiency, grade_itinerary_diversity

app = Flask(__name__)
env = TravelEnv()

# ── Core endpoints (Phase 1 — already passing) ─────────────

@app.route("/reset", methods=["POST"])
def reset():
    state = env.reset()
    return jsonify({"observation": state})

@app.route("/step", methods=["POST"])
def step():
    action = int(request.get_json()["action"])
    state, reward, done, info = env.step(action)
    return jsonify({"observation": state, "reward": reward, "done": done, "info": info})

@app.route("/state", methods=["GET"])
def state():
    return jsonify({"state": env.state()})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# ── Grader endpoints (Phase 2 — this was missing) ──────────

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "tasks": [
            {"id": "preference_match",    "description": "Agent picks place matching user preferences"},
            {"id": "budget_efficiency",   "description": "Agent stays within budget"},
            {"id": "itinerary_diversity", "description": "Agent explores diverse place types"},
        ]
    })

@app.route("/grade", methods=["POST"])
def grade():
    action = int(request.get_json()["action"])
    state  = env.state() or {"budget": 5000, "preferences": ["nature"], "day": 1}
    scores = {
        "preference_match":    grade_preference_match(action, state),
        "budget_efficiency":   grade_budget_efficiency(action, state),
        "itinerary_diversity": grade_itinerary_diversity(env.actions_history),
    }
    return jsonify({"scores": scores})

def main():
    app.run(host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
