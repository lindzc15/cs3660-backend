from pydantic import BaseModel
import os
from dotenv import load_dotenv
import httpx
import base64
import json
from fastapi import HTTPException

from models.favorite_pattern_model import FavoritePatterns
from models.favorite_yarn_model import FavoriteYarns
from models.user_model import User
from sqlalchemy.orm import Session

from schemas.ravelry_schema import (YarnResponse, YarnIDResponse, YarnID, YarnCompany, Weight, Fibers, Photo, 
FiberType, PatternBasics, PatternPhotoBasic, PatternsResponse, DesignerInfo, PatternID, PatternIDResponse)

from schemas.login_schema import RegisterResponse
from schemas.favorite_schema import FavoriteRequest

load_dotenv()  # Load variables from .env file

RAVELRY_USERNAME = os.getenv("RAVELRY_USERNAME")
RAVELRY_PASSWORD = os.getenv("RAVELRY_PASSWORD")


class FavoritesRepository:
    def __init__(self, db: Session):
        self.db = db


    def get_user_by_username(self, username: str) -> User:
        try:
            return self.db.query(User).filter(User.username == username).first()
        except Exception:
            self.db.rollback()
            raise

    def get_favorite_yarns(self, request: FavoriteRequest) -> YarnIDResponse:
        #check first that user exists
        user = self.get_user_by_username(request.username)
        if not user:
            raise ValueError("User not found")
        
        try:
            favorite_yarns = self.db.query(FavoriteYarns).filter(FavoriteYarns.username == request.username).all()

            if not favorite_yarns: 
                raise ValueError("No favorites found for this user")
            
            yarn_ids = [YarnID(id=str(yarn.yarn_id)) for yarn in favorite_yarns]

            return YarnIDResponse(yarnIDs= yarn_ids)
        except Exception:
            self.db.rollback()
            raise

    def add_favorite_yarn(self, request: FavoriteRequest) -> RegisterResponse:
        #check first that user exists
        user = self.get_user_by_username(request.username)
        if not user:
            raise ValueError("User not found")
        
        try:
            new_favorite = FavoriteYarns(
                username=request.username,
                yarn_id=request.id
            )

            self.db.add(new_favorite)
            self.db.commit()
            self.db.refresh(new_favorite)

            return RegisterResponse(success=True)

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))



    def delete_favorite_yarn(self, request: FavoriteRequest) -> RegisterResponse:
        #check first that user exists
        user = self.get_user_by_username(request.username)
        if not user:
            raise ValueError("User not found")
        
        try:
            favorite_yarn = self.db.query(FavoriteYarns).filter(
                FavoriteYarns.username == request.username,
                FavoriteYarns.yarn_id == request.id
            ).first()

            if not favorite_yarn:
                raise ValueError("Favorited yarn not found")

            self.db.delete(favorite_yarn)
            self.db.commit()

            return RegisterResponse(success=True)

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    

    def get_favorite_patterns(self, request: FavoriteRequest) -> PatternIDResponse:
        #check first that user exists
        user = self.get_user_by_username(request.username)
        if not user:
            raise ValueError("User not found")
        
        try:
            favorite_patterns = self.db.query(FavoritePatterns).filter(FavoritePatterns.username == request.username).all()

            if not favorite_patterns: 
                raise ValueError("No favorites found for this user")
            
            pattern_ids = [PatternID(id=str(pattern.pattern_id)) for pattern in favorite_patterns]

            return PatternIDResponse(patternIDs= pattern_ids)
        except Exception:
            self.db.rollback()
            raise

    def add_favorite_pattern(self, request: FavoriteRequest) -> RegisterResponse:
        #check first that user exists
        user = self.get_user_by_username(request.username)
        if not user:
            raise ValueError("User not found")
        
        try:
            new_favorite = FavoritePatterns(
                username=request.username,
                pattern_id=request.id
            )

            self.db.add(new_favorite)
            self.db.commit()
            self.db.refresh(new_favorite)

            return RegisterResponse(success=True)

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))



    def delete_favorite_pattern(self, request: FavoriteRequest) -> RegisterResponse:
        #check first that user exists
        user = self.get_user_by_username(request.username)
        if not user:
            raise ValueError("User not found")
        
        try:
            favorite_pattern = self.db.query(FavoritePatterns).filter(
                FavoritePatterns.username == request.username,
                FavoritePatterns.pattern_id == request.id
            ).first()

            if not favorite_pattern:
                raise ValueError("Favorited yarn not found")

            self.db.delete(favorite_pattern)
            self.db.commit()

            return RegisterResponse(success=True)

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))