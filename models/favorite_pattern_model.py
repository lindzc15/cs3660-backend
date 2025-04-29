from sqlalchemy import Column, String, PrimaryKeyConstraint
from models.base_model import Base

class FavoritePatterns(Base):
    __tablename__ = 'favorite_patterns'
    
    username = Column(String(50), nullable=False)
    pattern_id = Column(String(50), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('username', 'pattern_id'),
    )

    def __init__(self, username: str, pattern_id: str):
        self.username = username
        self.pattern_id = pattern_id
