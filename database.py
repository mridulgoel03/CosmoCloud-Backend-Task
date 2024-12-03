from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI from the environment
MONGO_URI = os.getenv("MONGO_URI")

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Reference the database
db = client.student_management
