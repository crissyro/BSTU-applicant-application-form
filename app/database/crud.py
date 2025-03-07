from pymongo import MongoClient
from config.settings import CONFIG


class Database:
    def __init__(self):
        self.client = MongoClient(CONFIG.MONGO_URI) 
        self.db = self.client.survey_bot
        self.users = self.db.users
        
        
    def save_answer(self, user_id: int, data: dict):
        try:
            self.users.update_one(
                {"user_id": user_id},
                {"$set": data},
                upsert=True
            )
            return True
        except Exception as e:
            print(f"Database error: {e}")
            return False

    def get_user_data(self, user_id: int):
        return self.users.find_one({"user_id": user_id})

    def clear_data(self, user_id: int):
        self.users.delete_one({"user_id": user_id})
            
db = Database()