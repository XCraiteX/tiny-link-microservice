from sqlalchemy.types import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase): 
    pass

class LinksTable(Base):
    __tablename__ = 'links'

    id: Mapped[String] = mapped_column(String, primary_key=True)
    link: Mapped[String] = mapped_column(String)
    views: Mapped[Integer] = mapped_column(Integer, default=0)
    limit: Mapped[Integer] = mapped_column(Integer, default=0)