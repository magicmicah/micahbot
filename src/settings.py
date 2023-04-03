import os
from os.path import join, dirname
from dotenv import load_dotenv
import logging

# Set the logging level and format
logger = logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

logger.info('Completed configuring logger()!') 
dotenv_file = join(dirname(__file__), '.env')
load_dotenv(dotenv_file)

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
RAPID_API_KEY = os.environ.get("RAPID_API_KEY")
DADJOKE_URL = os.environ.get("DADJOKE_URL")
STARTUP_IDEA_URL = os.environ.get("STARTUP_IDEA_URL")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
GIPHY_API_KEY=os.environ.get("GIPHY_API_KEY")
REPLICATE_API_TOKEN=os.environ.get("REPLICATE_API_TOKEN")

SQLITE_DB_FILE = os.environ.get("SQLITE_DB_FILE")