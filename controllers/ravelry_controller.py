from fastapi import APIRouter

from schemas.ravelry_schema import YarnResponse, YarnIDResponse, YarnID, PatternsResponse
from services.ravelry_service import RavelryService
router = APIRouter(prefix="/api/ravelry", tags=["ravelry", "yarns"])

@router.get("/yarns", response_model=YarnIDResponse)
async def yarns():
    return await RavelryService.get_all_yarns()

@router.post("/yarn/details", response_model=YarnResponse)
async def yarn_details(id: YarnID):
    return await RavelryService.get_yarn_details(id.id)

@router.get("/patterns", response_model=PatternsResponse)
async def patterns():
    return await RavelryService.get_all_patterns()

