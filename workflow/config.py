import os

from dotenv import load_dotenv


load_dotenv()

HOST = os.getenv('HOST', None)

TIKERS = os.getenv('TIKERS', None)
