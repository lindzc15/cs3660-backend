from pydantic import BaseModel
from typing import List, Optional

class YarnCompany(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None

class Photo(BaseModel):
    medium_url: Optional[str] = None

class Weight(BaseModel):
    name: Optional[str]

class FiberType(BaseModel):
    name: Optional[str]

class Fibers(BaseModel):
    percentage: Optional[int] = None
    fiber_type: Optional[FiberType] = None

class YarnResponse(BaseModel):
    id: int
    name: Optional[str] = None
    yarn_company: Optional[YarnCompany] = None
    photos: Optional[List[Photo]] = None
    yarn_weight: Optional[Weight] = None
    yarn_fibers: Optional[List[Fibers]] = None 

class YarnID(BaseModel):
    id: str

class YarnIDResponse(BaseModel):
    yarnIDs: List[YarnID]
