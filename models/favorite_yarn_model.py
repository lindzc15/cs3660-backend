from sqlalchemy import Column, String, PrimaryKeyConstraint
from models.base_model import Base

class FavoriteYarns(Base):
    __tablename__ = 'favorite_yarns'
    
    username = Column(String(50), nullable=False)
    yarn_id = Column(String(50), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('username', 'yarn_id'),
    )

    def __init__(self, username: str, yarn_id: str):
        self.username = username
        self.yarn_id = yarn_id