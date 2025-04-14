# containers.py
from dependency_injector import containers, providers

from db.db import DatabaseFactory, get_db_session
from repositories.user_repository import UserRepository
from services.login_service import LoginService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["controllers.login_controller"])

    db_session = providers.Resource(get_db_session)

    user_repository = providers.Factory(
        UserRepository,
        db=db_session
    )

    login_service = providers.Factory(
        LoginService,
        user_repository=user_repository
    )
