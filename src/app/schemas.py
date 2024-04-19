from datetime import date
from dataclasses import dataclass


@dataclass
class User:
    username: str
    email: str
    password: str
    email_verified: bool = False
    birthday: date | None = None
