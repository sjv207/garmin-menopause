from dotenv import load_dotenv
import os

# These are derived first from environment variables
OFF_MODEL_HOST = os.getenv('GC_OFF_MODEL_HOST')
OFF_MODEL_USERNAME = os.getenv('GC_OFF_MODEL_USERNAME')
OFF_MODEL_PASSWORD = os.getenv('GC_OFF_MODEL_PASSWORD')
OFF_MODEL_DATABASE = os.getenv('GC_OFF_MODEL_DATABASE')
