from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.models.GameModel import GameCreate, GameUpdate
from db.database import Game, SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_game(game_id: int, db: Session = Depends(get_db)):
    return db.query(Game, game_id).first()


def get_game_by_igdb_ig(igdb_id, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.igdb_id == igdb_id).first()
    if game is not None:
        return game
    else:
        return JSONResponse(status_code=404, content={"message": "No game with this igdb_id"})


def get_games(db: Session = Depends(get_db)):
    games = db.query(Game).all()
    for p in games:
        print(f"{p.id}.{p.name} ({p.age})")
    return games


def create_game(game_create: GameCreate, db: Session = Depends(get_db)):
    game = Game(igdb_id=game_create.igdb_id, title=game_create.title)
    if game_create.cover_url is not None:
        game.cover_url = game_create.cover_url
    db.add(game)
    db.commit()
    print(game.id)
    return game


def delete_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    db.delete(game)
    db.commit()


def update_game(game_upd: GameUpdate, db: Session = Depends(get_db)):
    game = db.query(Game, game_upd.id).first()

    if game is None:
        return JSONResponse(status_code=404, content={"message": "Game not found"})

    if game_upd.userRating is not None:
        game.userRating = game_upd.userRating
    if game_upd.status is not None:
        game.userRating = game_upd.status

    db.commit()
    db.refresh(game)
    print(game)
    return game
