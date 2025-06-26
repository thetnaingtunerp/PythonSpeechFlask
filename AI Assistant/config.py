import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
