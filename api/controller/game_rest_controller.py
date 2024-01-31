from fastapi import APIRouter

game_routes = APIRouter()


@game_routes.get("/game/{game_id}")
def get_game(game_id: int):
    return game_id


@game_routes.get("/game/{igdb_id}")
def get_game_by_igdb_ig(igdb_id: int):
    return igdb_id


@game_routes.get("/games")
def get_games():
    return 0


@game_routes.post("/game")
def create_game():
    return 0


@game_routes.delete("/game/{game_id}")
def create_game(game_id: int):
    return game_id


@game_routes.delete("/game/{game_id}")
def delete_game(game_id: int):
    return game_id


@game_routes.delete("/game/{game_id}")
def update_game(game_id: int):
    return game_id

