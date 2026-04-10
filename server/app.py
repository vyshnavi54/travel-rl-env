import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openenv.core.env_server import create_app
from models import TravelAction, TravelObservation
from server.travel_environment import TravelEnvironment

app = create_app(TravelEnvironment, TravelAction, TravelObservation, env_name="travel_planner_env")

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
