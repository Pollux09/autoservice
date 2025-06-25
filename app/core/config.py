from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)
    HOST: str = "localhost"
    PORT: int = "8888"
    RELOAD: bool = True
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str = "fc75c87e64ff204fa7be65db214ad07c"
    ALGORITHM: str = "HS256"

    @property
    def server_host(self) -> str:
        if self.ENVIRONMENT == "local":
            return f"http://{self.HOST}:{self.PORT}"
        return f"https://{self.HOST}:{self.PORT}"

    POSTGRES_SERVER: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "autoservice"

    ECHO: bool
    ECHO_POOL: bool
    POOL_SIZE: int
    MAX_OVERFLOW: int

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> MultiHostUrl:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()
