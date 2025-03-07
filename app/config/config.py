from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    MONGO_URI: str
    ADMIN_IDS: int
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

config = Settings()