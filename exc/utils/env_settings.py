from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "local"
    DB_HOST: str = "=127.0.0.1"
    DB_DATABASE: str
    DB_USER: str
    DB_PASSWORD: str
    echo_sql: bool = True
    test: bool = False
    oauth_token_secret: str = "my_dev_secret"

settings = Settings()