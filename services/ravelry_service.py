from repositories.ravelry_repository import RavelryRepository
from schemas.ravelry_schema import YarnResponse, YarnIDResponse, PatternsResponse
from typing import List, Optional

class RavelryService:
    @staticmethod
    async def get_all_yarns() -> YarnIDResponse | None:
        return await RavelryRepository.get_all_yarns()
    
    @staticmethod
    async def get_yarn_details(id) -> YarnResponse | None:
        return await RavelryRepository.get_yarn_details(id)

    @staticmethod
    async def get_all_patterns() -> PatternsResponse | None:
        return await RavelryRepository.get_all_patterns()
    
    @staticmethod
    async def search_patterns(query) -> PatternsResponse | None:
        return await RavelryRepository.search_patterns(query)
    
    @staticmethod
    async def search_yarns(query) -> YarnIDResponse | None:
        return await RavelryRepository.search_yarns(query)