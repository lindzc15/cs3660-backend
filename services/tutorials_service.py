from repositories.tutorials_repository import TutorialsRepository
from schemas.tutorials_schema import TutorialResponse
from typing import List, Optional

class TutorialService:
    @staticmethod
    async def get_tutorials() -> TutorialResponse | None:
        return await TutorialsRepository.get_tutorials()
    