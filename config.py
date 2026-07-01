from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL", "gpt-5")
BOT_NAME = os.getenv("BOT_NAME","Nova")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
