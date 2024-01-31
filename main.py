from fastapi import FastAPI

from api.controller.game_rest_controller import game_routes
from api.controller.igdb_games_controller import igdb_games_routes

app = FastAPI()
app.include_router(game_routes, prefix="/api", tags=["Game"])
app.include_router(igdb_games_routes, prefix="/api/igdb", tags=["Igdb"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
