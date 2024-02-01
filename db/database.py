import enum

from sqlalchemy import create_engine, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', connect_args={"check_same_thread": False})
Base = declarative_base()


class StatusEnum(enum.Enum):
    COMPLETED = "Completed"
    PLAYING = "Playing"
    PLANNED = "Planned"
    ABANDONED = "Abandoned"


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer)
    title = Column(String)
    status = Column(Enum(StatusEnum))
    user_rating = Column(Float)
    cover_url = Column(String)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
