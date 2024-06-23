from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, select

from database import get_session
from models import Album, Band, BandCreate, GenreURLChoices

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'ACDC', 'genre': 'Metal'},
    {'id': 2, 'name': 'PVRIS', 'genre': 'Rock'},
    {'id': 3, 'name': 'one direction', 'genre': 'pop'},
    {'id': 4, 'name': 'imagine dragons', 'genre': 'Rock'},
    {'id': 5, 'name': 'chainsmokers', 'genre': 'hip hop'},
    {'id': 6, 'name': 'Eurythmics', 'genre': 'Electronic'}
]

# Checkout /docs swagger api docs thing is amazing


@app.get("/")
def Home(genre: GenreURLChoices | None = None,
         q: Annotated[str | None, Query(max_length=10)] = None,
         session: Session = Depends(get_session)
         ) -> list[Band]:
    band_query = session.exec(select(Band)).all()
    if band_query is None:
        raise HTTPException(status_code=404, detail='Not Found')
    if genre:
        band_query = [b for b in band_query if b.genre.lower() == genre.value.lower()]
    if q:
        band_query = [b for b in band_query if q.lower() in b.name.lower()]
        return band_query
    return band_query


@app.get('/bands/{band_id}')
async def band(band_id: int, session: Session = Depends(get_session)) -> Band:
    band = session.get(Band, band_id)
    if band is None:
        raise HTTPException(status_code=404, detail='Not Found')
    return band


@app.post("/bands")
async def create_band(band_data: BandCreate, session: Session = Depends(get_session)) -> Band:
    band = Band(name=band_data.name, genre=band_data.genre)
    session.add(band)

    if band_data.album:
        for album in band_data.album:
            album_object = Album(
                title=album.title, release_date=album.release_date, band=band)
        session.add(album_object)
    session.commit()
    session.refresh(band)
    return band
