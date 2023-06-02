from typing import Dict

from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    id: str
    seat_map: Dict[str,bool] #dictionary to track seat availability

class Booking(BaseModel):
    movie_id: str
    seat_id: str

