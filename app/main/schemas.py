from pydantic import BaseModel

class Link(BaseModel):
    link: str
    limit: int = 0
    