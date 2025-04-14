import json

from fastapi import HTTPException

from models.user_model import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(self, username: str) -> User:
        try:
            return self.db.query(User).filter(User.username == username).first()
        except Exception:
            self.db.rollback()
            raise

    def register_user(self, user: User) -> User:
        existing_user = self.get_user_by_username(user.username)
        if existing_user:
            raise ValueError("Username already registered")

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

        
        
                
            