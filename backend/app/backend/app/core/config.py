from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://gitpod@localhost:5432/spec_tech_bot"
    SECRET_KEY: str = "ваш_ключ_для_теста"
    WATBOT_API_KEY: str = ""
    WATBOT_BOT_ID: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
