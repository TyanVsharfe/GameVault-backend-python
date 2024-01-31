import configparser

from fastapi import APIRouter
import requests

from api.service.request_igdb_service import get_igdb_api_key

igdb_games_routes = APIRouter()


@igdb_games_routes.post("/games/{game_name}")
def get_igdb_games(game_name: str):
    key_api = get_igdb_api_key()
    config = configparser.ConfigParser()
    config.read('config.ini')

    headers = {
        "Client-ID": config["IGDB_API"]["client_id"],
        "Authorization": f"Bearer {key_api['access_token']}",
        "Content-Type": "text/plain"
    }

    body = (
        f"""
        fields name,cover.url,release_dates.y,platforms,platforms.abbreviation,aggregated_rating,
        first_release_date,category;
        search "{game_name}";
        where category = (0,8,9) & version_parent = null;
        limit 200;
        """
    )

    response = requests.post("https://api.igdb.com/v4/games", headers=headers, data=body)
    print(response.json())
    return response.json()


@igdb_games_routes.post("/game/{game_id}")
def get_igdb_games(game_id: int):

    key_api = get_igdb_api_key()
    config = configparser.ConfigParser()
    config.read('config.ini')

    headers = {
        "Client-ID": config["IGDB_API"]["client_id"],
        "Authorization": f"Bearer {key_api['access_token']}",
        "Content-Type": "text/plain"
    }

    body = f"fields name,cover.url,release_dates.y,status,category,summary,genres.name,first_release_date,platforms.abbreviation; where id = {game_id};"

    response = requests.post("https://api.igdb.com/v4/games", headers=headers, data=body)
    print(response.json())
    return response.json()

