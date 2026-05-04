from dataclasses import dataclass
from datetime import datetime

@dataclass
class PasswordRecord:
    service: str
    username: str
    password: str
    created_at: str

    @staticmethod
    def create(service, username, password):
        return PasswordRecord(
            service=service,
            username=username,
            password=password,
            created_at=str(datetime.now())
        )
