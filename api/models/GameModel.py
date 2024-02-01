from pydantic import BaseModel

from db.database import StatusEnum


class GameCreate(BaseModel):
    igdb_id: int
    title: str
    cover_url: str | None = None


class GameUpdate(BaseModel):
    id: int
    igdb_id: int
    status: StatusEnum
    userRating: float
