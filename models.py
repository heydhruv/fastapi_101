from enum import Enum
from datetime import date
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HOP_HOP = 'hop hop'
    POP = 'pop'



class AlbumBase(SQLModel):
    title: str
    release_date: date
    band_id: int = Field(foreign_key="band.id")

class Album(AlbumBase, table=True):
    id: int = Field(default=None, primary_key=True)
    band: "Band" = Relationship(back_populates="albums")


class BandBase(SQLModel):
    name: str
    genre: str

class BandCreate(BandBase):
    album: list[AlbumBase] | None = None


class Band(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")
