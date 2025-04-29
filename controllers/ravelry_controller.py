from fastapi import APIRouter

from schemas.ravelry_schema import YarnResponse, YarnIDResponse, YarnID, PatternsResponse, Search, PatternIDResponse, PatternID, PatternBasics
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

@router.post("/patterns/details", response_model=PatternBasics)
async def patterns(id: PatternID):
    return await RavelryService.get_pattern_details(id.id)

@router.post("/patterns/search", response_model=PatternsResponse)
async def patterns(query: Search):
    return await RavelryService.search_patterns(query.query)

@router.post("/yarns/search", response_model=YarnIDResponse)
async def patterns(query: Search):
    return await RavelryService.search_yarns(query.query)


