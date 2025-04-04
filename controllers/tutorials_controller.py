from fastapi import APIRouter, HTTPException

from schemas.tutorials_schema import TutorialResponse
from services.tutorials_service import TutorialService


router = APIRouter(prefix="/api/tutorials", tags=["Tutorials"])

@router.get("/", response_model=TutorialResponse)
async def tutorials():
    return await TutorialService.get_tutorials()