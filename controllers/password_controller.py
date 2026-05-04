from models.password_record import PasswordRecord

class PasswordController:
    def __init__(self, storage, password_service):
        self.storage = storage
        self.password_service = password_service
        self.records = self.storage.load()

    def add_record(self, service, username, password):
        record = PasswordRecord.create(service, username, password)
        self.records.append(record)

    def delete_record(self, index):
        if 0 <= index < len(self.records):
            self.records.pop(index)
            return True
        return False

    def list_records(self):
        return self.records

    def save(self):
        self.storage.save(self.records)
