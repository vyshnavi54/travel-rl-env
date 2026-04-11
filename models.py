try:
    from openenv.core.env_server.types import Action, Observation
except ImportError:
    from openenv.core.env_server.types import Action, Observation

from pydantic import Field

class TravelAction(Action):
    action: int = Field(..., description="0=Beach, 1=Temple, 2=Park")

class TravelObservation(Observation):
    budget: int = Field(default=5000)
    preferences: list = Field(default_factory=list)
    day: int = Field(default=1)
    place_visited: str = Field(default="")
    task_id: str = Field(default="easy")
