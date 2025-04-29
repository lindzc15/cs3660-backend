import hashlib
from fastapi import HTTPException
import jwt
import datetime
from repositories.user_repository import UserRepository
from models.user_model import User
from config import settings

class LoginService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    # Function to verify a jwt token
    def verify_token(self, token: str) -> dict:
        try:
            # Decode token
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
    
    #hashes passwords during new account creation, before storing in database
    def hash_password(self, username: str, password: str, name: str):
        if not username or not password or not name:
            raise Exception("Missing required fields")
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User(username, name, hashed_password)

        try:
            self.user_repository.register_user(user)
        except Exception as e:
            raise Exception(f"{str(e)}")
        
    # Function to verify login from users.json    
    def get_login_token(self, username: str, password: str) -> str:
        try:
            # Fetch user from database
            user = self.user_repository.get_user_by_username(username)
            if not user:
                raise Exception("User not found")

            # Hash input password using SHA256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Verify password match
            if user.password_hash != hashed_password:
                raise Exception("Invalid credentials")
            
            user_payload = {
                "username": user.username,
                "name": user.name
            }

            # Generate JWT token
            expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
            token_payload = {
                "sub": user.username,  # Subject (user)
                "exp": expiration_time,  # Expiry time
                "user": user_payload  # Include role or other user attributes if needed
            }
            token = jwt.encode(token_payload, settings.secret_key, algorithm=settings.algorithm)

            return token
        except Exception as e:
            raise Exception(f"Login failed: {str(e)}")
        
    #update a user's info in the database, return new token
    def update_user(self, username: str, name: str, old_username: str) -> str:
        try:
            user = self.user_repository.update_user(username, name, old_username)

            if not user:
                raise Exception("Error updating user")


            user_payload = {
                    "username": user.username,
                    "name": user.name
                }

            # Generate JWT token
            expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
            token_payload = {
                    "sub": user.username,  # Subject (user)
                    "exp": expiration_time,  # Expiry time
                    "user": user_payload  # Include role or other user attributes if needed
                }
            token = jwt.encode(token_payload, settings.secret_key, algorithm=settings.algorithm)

            return token
        except Exception as e:
            raise Exception(f"Login failed: {str(e)}")

