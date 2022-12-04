import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_file = join(dirname(__file__), '.env')
load_dotenv(dotenv_file)

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
RAPID_API_KEY = os.environ.get("RAPID_API_KEY")
DADJOKE_URL = os.environ.get("DADJOKE_URL")
STARTUP_IDEA_URL = os.environ.get("STARTUP_IDEA_URL")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

SQLITE_DB_FILE = os.environ.get("SQLITE_DB_FILE")