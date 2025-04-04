from pydantic import BaseModel
from typing import List

# Define request model
class Tutorial(BaseModel):
    name: str
    creator: str
    description: str
    link: str

class TutorialResponse(BaseModel):
    tutorials: List[Tutorial]