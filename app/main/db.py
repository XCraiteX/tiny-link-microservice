from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import select

from main import schemas, services
from main.models import LinksTable, Base

from data.settings import SERVICE_LINK

engine = create_async_engine('sqlite+aiosqlite:///data/links.db')
session = async_sessionmaker(bind=engine, class_=AsyncSession)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_short_link(lnk_obj: schemas.Link):
    key = await services.generate_key()

    async with session() as db:
        result = await db.execute(select(LinksTable).filter(LinksTable.link == lnk_obj.link))
        fetched = result.scalars().first()

        if fetched: 
            return {'status': 'OK', 'shorted': SERVICE_LINK + fetched.id, 'views': fetched.views}
        
        obj = LinksTable(id=key, link=lnk_obj.link, limit=lnk_obj.limit)
        views, key = obj.views, obj.id
        
        db.add(obj)
        await db.commit()

        return {'status': 'OK', 'shorted': SERVICE_LINK + key, 'views': 0}



async def go_link(key: str):
    async with session() as db:
        result = await db.execute(select(LinksTable).filter(LinksTable.id == key))
        fetched = result.scalars().first()

        if not fetched:
            return None
        
        link = fetched.link

        fetched.views += 1
        
        if fetched.limit > 0:
            if fetched.limit == fetched.views:
                await db.delete(fetched)
        
        await db.commit()

        return link

     