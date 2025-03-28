import json

from fastapi import HTTPException

from models.user_model import User


class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> User:
        try:
            with open("./db/users.json", "r") as file:
                data = json.load(file)
                for user in data["users"]:
                    if user["username"] == username:
                        return User(user["username"], user["name"], user["password_hash"])  # Returns the User object
        except FileNotFoundError:
            raise Exception("User file not found")
        return None
    

    @staticmethod
    def register_user(user: User):
        user_dict = user.to_dict()

        try:
            with open("./db/users.json", "r") as file:
                data = json.load(file)
                for user in data["users"]:
                    if user["username"] == user_dict["username"]:
                        raise Exception("Email already registered")
        except FileNotFoundError:
            raise Exception("File not found")

        try:
            data["users"].append(user_dict)
        except:
            raise Exception("bad stuff")

        with open("./db/users.json", "w") as f:
            json.dump(data, f)

        
        
                
            