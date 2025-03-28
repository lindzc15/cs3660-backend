class User:
    def __init__(self, username: str, name: str, password_hash: str):
        self.username = username
        self.name = name        
        self.password_hash = password_hash

    def to_dict(self):
        return {
            "username": self.username,
            "name": self.name,
            "password_hash": self.password_hash
        }