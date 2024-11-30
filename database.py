from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv('MONGO_DB_PASSWORD')

# MongoDB Connection URI
MONGO_DB_URI = f"mongodb+srv://adityagarg0911:{password}@cluster0.ybq8e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your MongoDB URI

client = AsyncIOMotorClient(MONGO_DB_URI)
db = client["student_management"]
students_collection = db["students"]


# from motor.motor_asyncio import AsyncIOMotorClient

# class Database:
#     def __init__(self, uri: str, db_name: str):
#         self.client = AsyncIOMotorClient(uri)
#         self.db = self.client[db_name]

# # Replace with your MongoDB Atlas connection string
# MONGO_URI = "mongodb+srv://adityagarg0911:DupshuxD0vbjf6JK@cluster0.ybq8e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# DB_NAME = "student_management"

# db = Database(MONGO_URI, DB_NAME)
# students_collection = db["students"]