from fastapi import APIRouter

from api.models.GameModel import GameCreate
from api.service import game_service

game_routes = APIRouter()


@game_routes.get("/game/{game_id}")
def get_game(game_id: int):
    game_service.get_game(game_id)


@game_routes.get("/game/{igdb_id}")
def get_game_by_igdb_ig(igdb_id: int):
    game_service.get_game_by_igdb_ig(igdb_id)


@game_routes.get("/games")
def get_games():
    game_service.get_games()


@game_routes.post("/game")
def create_game(game_create: GameCreate):
    game_service.create_game(game_create)


@game_routes.delete("/game/{game_id}")
def delete_game(game_id: int):
    game_service.delete_game(game_id)


@game_routes.put("/game/{game_id}")
def update_game(game_id: int):
    return game_id

