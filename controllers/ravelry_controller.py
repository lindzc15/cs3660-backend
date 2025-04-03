from fastapi import APIRouter

from schemas.ravelry_schema import YarnResponse, YarnIDResponse, YarnID
from services.ravelry_service import RavelryService
from schemas.message_schema import MessageResponse
router = APIRouter(prefix="/api/ravelry", tags=["ravelry", "yarns"])

@router.get("/yarns", response_model=YarnIDResponse)
async def yarns():
    return await RavelryService.get_all_yarns()

@router.post("/yarn/details", response_model=YarnResponse)
async def yarn_details(id: YarnID):
    return await RavelryService.get_yarn_details(id.id)


