import os

from dotenv import load_dotenv


load_dotenv()

TG_AP = os.getenv('TG_AP', None)
