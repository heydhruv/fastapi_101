from fastapi import FastAPI, HTTPException
from schemas import BandWithID, BandCreate
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
def Home() -> list[BandWithID]:
    return [
        BandWithID(**b) for b in BANDS
    ]

@app.get('/bands/{band_id}')
async def band(band_id: int) -> BandWithID:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='Not Found')
    return band

@app.get("/about")
def About() -> str :
    return "Amazing Company"


@app.post("/bands")
async def create_band(band_data: BandCreate) -> BandWithID:
    id = BANDS[-1]['id'] + 1
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band
