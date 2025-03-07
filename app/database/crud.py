from pymongo import MongoClient
from config.settings import CONFIG


class Database:
    def __init__(self):
        self.client = MongoClient(CONFIG.MONGO_URI) 
        self.db = self.client.survey_bot
        self.users = self.db.users
        
        
    def get_user(self, user_id):
        return self.users.find_one({"user_id": user_id})
    
    def update_user(self, user_id, data):
        return self.users.update_one({"user_id": user_id}, {"$set": data}, upsert=True)
    
    def get_dump(self):
        return list(self.users.find({}, {"_id": 0}))
            
db = Database()