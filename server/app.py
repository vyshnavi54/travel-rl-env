import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from openenv.core.env_server import create_app
except ImportError:
    from openenv.core.env_server import create_app

try:
    from ..models import TravelAction, TravelObservation
except ImportError:
    from models import TravelAction, TravelObservation

try:
    from .travel_environment import TravelEnvironment, TASKS, GRADERS, PLACE_INFO
except ImportError:
    from server.travel_environment import TravelEnvironment, TASKS, GRADERS, PLACE_INFO

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Base app from OpenEnv
app = create_app(TravelEnvironment, TravelAction, TravelObservation, env_name="travel_planner_env")

# ── /tasks endpoint — validator checks this for graders ──────────────
@app.get("/tasks")
def get_tasks():
    return JSONResponse({
        "tasks": [
            {
                "id":          "easy",
                "name":        "Preference Match",
                "description": "Pick a place matching user preferences",
                "grader":      "grade_easy",
                "score_range": [0, 1],
            },
            {
                "id":          "medium",
                "name":        "Budget Efficiency",
                "description": "Stay within budget",
                "grader":      "grade_medium",
                "score_range": [0, 1],
            },
            {
                "id":          "hard",
                "name":        "Itinerary Diversity",
                "description": "Explore diverse place types",
                "grader":      "grade_hard",
                "score_range": [0, 1],
            },
        ]
    })

# ── /grade endpoint — validator calls this to check scores ───────────
class GradeRequest(BaseModel):
    task_id: str = "easy"
    action: int = 1
    state: dict = {}
    actions_history: list = []

@app.post("/grade")
def grade(req: GradeRequest):
    task_id = req.task_id if req.task_id in TASKS else "easy"
    if task_id == "hard":
        history = req.actions_history or [req.action]
        score = GRADERS["hard"](history)
    elif task_id == "medium":
        score = GRADERS["medium"](req.action, req.state or {"budget": 5000})
    else:
        score = GRADERS["easy"](req.action, req.state or {"preferences": ["nature"]})

    assert 0 < score < 1, f"Score out of range: {score}"
    return JSONResponse({"task_id": task_id, "score": score})

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
