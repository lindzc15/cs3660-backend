from repositories.favorites_repository import FavoritesRepository
from schemas.ravelry_schema import YarnResponse, YarnIDResponse, PatternsResponse, PatternIDResponse
from schemas.login_schema import RegisterResponse
from typing import List, Optional

class FavoritesService:
    def __init__(self, favorites_repository: FavoritesRepository):
        self.favorites_repository = favorites_repository

    def get_favorite_yarns(self, request) -> YarnIDResponse | None:
        return self.favorites_repository.get_favorite_yarns(request)

    def add_favorite_yarn(self, request) -> RegisterResponse | None:
        return self.favorites_repository.add_favorite_yarn(request)
    
    def delete_favorite_yarn(self, request) -> RegisterResponse | None:
        return self.favorites_repository.delete_favorite_yarn(request)

    def get_favorite_patterns(self, request) -> PatternIDResponse | None:
        return self.favorites_repository.get_favorite_patterns(request)

    def add_favorite_pattern(self, request) -> RegisterResponse | None:
        return self.favorites_repository.add_favorite_pattern(request)
    
    def delete_favorite_pattern(self, request) -> RegisterResponse | None:
        return self.favorites_repository.delete_favorite_pattern(request)
