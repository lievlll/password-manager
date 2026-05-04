import json
from models.password_record import PasswordRecord

class StorageService:
    FILE_PATH = "data/passwords.json"

    def load(self):
        try:
            with open(self.FILE_PATH, "r") as f:
                data = json.load(f)
                return [PasswordRecord(**item) for item in data]
        except:
            return []

    def save(self, records):
        with open(self.FILE_PATH, "w") as f:
            json.dump([r.__dict__ for r in records], f, indent=4)
