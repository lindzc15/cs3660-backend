from dependency_injector import containers, providers

from db.db import get_db_session
from repositories.user_repository import UserRepository
from repositories.favorites_repository import FavoritesRepository
from services.login_service import LoginService
from services.favorites_service import FavoritesService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "controllers.login_controller",
            "controllers.favorites_controller" 
        ]
    )

    db_session = providers.Resource(get_db_session)

    # Repositories
    user_repository = providers.Factory(
        UserRepository,
        db=db_session
    )

    favorites_repository = providers.Factory(  
        FavoritesRepository,
        db=db_session
    )

    # Services
    login_service = providers.Factory(
        LoginService,
        user_repository=user_repository
    )

    favorites_service = providers.Factory( 
        FavoritesService,
        favorites_repository=favorites_repository
    )

