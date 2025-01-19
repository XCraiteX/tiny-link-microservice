from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from main import db, schemas, services
from data.settings import DEFAULT_LINK

app = FastAPI()

# Create Short Link
@app.post('/lnk/api')
async def create_short(link: schemas.Link):
    valid = await services.valid_link(link.link)
    
    if valid: 
        return await db.create_short_link(link)
    
    return {'status': 'Error', 'details': 'Invalid link'}


# Open Shorted Link
@app.get('/lnk/{key}')
async def go_link(key):
    link = await db.go_link(key)

    if link: 
        return RedirectResponse(url=link)
    
    return RedirectResponse(url=DEFAULT_LINK)


@app.on_event('startup')
async def startup():
    await db.create_tables()


# uvicorn api:app --reload