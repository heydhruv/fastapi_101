from enum import Enum
from datetime import date
from pydantic import BaseModel


class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HOP_HOP = 'hop hop'
    POP = 'pop'


class Album(BaseModel):
    title: str
    release_date: date

class BandBase(BaseModel):
    name: str
    genre: str
    album: list[Album] = []

class BandCreate(BandBase):
    pass

class BandWithID(BandBase):
    id: int

