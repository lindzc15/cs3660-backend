from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import settings


class DatabaseFactory:
    def __init__(self):
        self.engine = create_engine(settings.database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def close_session(self):
        self.db.close()

    def get_session(self):
        return self.SessionLocal()    
    

db_factory = DatabaseFactory()

def get_db_session():
    db = db_factory.get_session()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()