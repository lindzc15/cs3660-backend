from pydantic import BaseModel
from typing import Optional


class FavoriteRequest(BaseModel):
    username: str
    id: Optional[str] = None