from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str
    allow_origins: list[AnyHttpUrl] 
    api_gateway_token: str
    ravelry_username: str
    ravelry_password: str

    class Config:
        env_file = ".env"


settings = Settings()