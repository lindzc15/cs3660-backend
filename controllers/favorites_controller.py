from fastapi import APIRouter, HTTPException, Depends

from dependency_injector.wiring import Provide, inject
from containers import Container
from schemas.ravelry_schema import YarnResponse, YarnIDResponse, YarnID, PatternsResponse, PatternIDResponse
from schemas.login_schema import RegisterResponse
from schemas.favorite_schema import FavoriteRequest
from services.favorites_service import FavoritesService


router = APIRouter(prefix="/api/favorites", tags=["Favorites"])

@router.post("/yarn/all", response_model= YarnIDResponse)
@inject
def get_favorite_yarns(request: FavoriteRequest,
                             favorite_service: FavoritesService = Depends(Provide[Container.favorites_service])):
    return favorite_service.get_favorite_yarns(request)

@router.post("/yarn", response_model= RegisterResponse)
@inject
def add_favorite_yarn(request: FavoriteRequest,
                            favorite_service: FavoritesService = Depends(Provide[Container.favorites_service])):
    return favorite_service.add_favorite_yarn(request)

@router.delete("/yarn", response_model= RegisterResponse)
@inject
def delete_favorite_yarn(request: FavoriteRequest,
                               favorite_service: FavoritesService = Depends(Provide[Container.favorites_service])):
    return favorite_service.delete_favorite_yarn(request)



@router.post("/pattern/all", response_model= PatternIDResponse)
@inject
def get_favorite_patterns(request: FavoriteRequest,
                                favorite_service: FavoritesService = Depends(Provide[Container.favorites_service])):
    return favorite_service.get_favorite_patterns(request)

@router.post("/pattern", response_model= RegisterResponse)
@inject
def add_favorite_pattern(request: FavoriteRequest,
                               favorite_service: FavoritesService = Depends(Provide[Container.favorites_service])):
    return favorite_service.add_favorite_pattern(request)

@router.delete("/pattern", response_model= RegisterResponse)
@inject
def delete_favorite_pattern(request: FavoriteRequest,
                                  favorite_service: FavoritesService = Depends(Provide[Container.favorites_service])):
    return favorite_service.delete_favorite_pattern(request)

