from pydantic import BaseModel
import os
from dotenv import load_dotenv
import httpx
import base64
import json

from schemas.ravelry_schema import (YarnResponse, YarnIDResponse, YarnID, YarnCompany, Weight, Fibers, Photo, 
FiberType, PatternBasics, PatternPhotoBasic, PatternsResponse, DesignerInfo)

from schemas.login_schema import RegisterResponse

load_dotenv()  # Load variables from .env file

RAVELRY_USERNAME = os.getenv("RAVELRY_USERNAME")
RAVELRY_PASSWORD = os.getenv("RAVELRY_PASSWORD")


class RavelryRepository:
    @staticmethod
    async def get_all_yarns() -> YarnIDResponse | None:
        all_url = "https://api.ravelry.com/yarns/search.json"
        credentials = f"{RAVELRY_USERNAME}:{RAVELRY_PASSWORD}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        headers = {"Authorization": f"Basic {encoded_credentials}"}
        all_yarns = []
        async with httpx.AsyncClient(timeout=30) as client:
            for page in range(1,2):
                response = await client.get(f"{all_url}?page_size=16&page={page}", headers=headers)
                if response.status_code == 200:
                    yarn_data = response.json()
                    
                    yarn_ids = [YarnID(id=str(yarn["id"])) for yarn in yarn_data["yarns"]]
                    return YarnIDResponse(yarnIDs=yarn_ids)
                return None
                    
    @staticmethod
    async def get_yarn_details(id: str) -> YarnResponse | None:
        url = f"https://api.ravelry.com/yarns/{id}.json"
        credentials = f"{RAVELRY_USERNAME}:{RAVELRY_PASSWORD}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        headers = {"Authorization": f"Basic {encoded_credentials}"}
        async with httpx.AsyncClient(timeout=30) as client: 
            response = await client.get(f"{url}", headers=headers)
            if response.status_code == 200:
                yarn_details = response.json()
                yarn_data = yarn_details["yarn"]
                

                return YarnResponse(
                    id=yarn_data.get("id"),
                    name=yarn_data.get("name"),
                    yarn_company=YarnCompany(**yarn_data["yarn_company"]) if "yarn_company" in yarn_data else None,
                    photos=[Photo(medium_url=photo["medium_url"]) for photo in yarn_data.get("photos", [])],
                    yarn_weight=Weight(name=yarn_data["yarn_weight"].get("name") if "yarn_weight" in yarn_data else None),
                    yarn_fibers=[
                        Fibers(percentage=fiber["percentage"], fiber_type=FiberType(name=fiber["fiber_type"].get("name")))
                        for fiber in yarn_data.get("yarn_fibers", [])
                    ] if "yarn_fibers" in yarn_data else None)
            return None
        
    
    @staticmethod
    async def get_all_patterns() -> PatternsResponse | None:
        all_url = "https://api.ravelry.com/patterns/search.json"
        credentials = f"{RAVELRY_USERNAME}:{RAVELRY_PASSWORD}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        headers = {"Authorization": f"Basic {encoded_credentials}"}

        async with httpx.AsyncClient(timeout=30) as client: 
            response = await client.get(all_url, headers=headers)
            if response.status_code == 200:
                pattern_data = response.json()
                patternStuff = pattern_data.get("patterns", [])
                
                print(type(patternStuff))
                for pattern in patternStuff:
                    print(f"id {pattern['id']}")

                pattern_basics_list = [
                    PatternBasics(                    
                        id=str(pattern["id"]),
                        free=pattern["free"],
                        name=pattern["name"],
                        designer=DesignerInfo(**pattern["designer"]) if "designer" in pattern else None,
                        first_photo=PatternPhotoBasic(medium_url=pattern["first_photo"]["medium_url"]) if "first_photo" in pattern else None
                    )
                    for pattern in patternStuff
                ]

                return PatternsResponse(patterns=pattern_basics_list)

        return None  
    

