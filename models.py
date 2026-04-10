from pydantic import Field
from openenv.core.env_server.types import Action, Observation

class TravelAction(Action):
    action: int = Field(..., description="0=Beach, 1=Temple, 2=Park")

class TravelObservation(Observation):
    budget: int = Field(..., description="Remaining budget")
    preferences: list = Field(..., description="User preferences")
    day: int = Field(..., description="Current day")
    place_visited: str = Field(default="", description="Place visited this step")