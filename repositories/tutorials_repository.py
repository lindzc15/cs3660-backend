import json
from fastapi import HTTPException
from schemas.tutorials_schema import TutorialResponse, Tutorial

class TutorialsRepository:
    @staticmethod
    async def get_tutorials():
        # Open the JSON file and load the data
        with open("./db/tutorials.json", "r") as file:
            data = json.load(file)
            tutorials = []  # List to store tutorial data

            # Iterate through the tutorials in the JSON data
            for tutorial in data["tutorials"]:
                # Create Tutorial object for each tutorial and append to the list
                tutorials.append(Tutorial(
                    name=tutorial["name"],
                    creator=tutorial["creator"],
                    link=tutorial["link"],
                    description=tutorial["description"]
                ))

            # Return the response with the list of tutorials
            return TutorialResponse(tutorials=tutorials)