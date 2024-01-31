import configparser
import os

import requests


def get_igdb_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')

    params = {
        "client_id": config["IGDB_API"]["client_id"],
        "client_secret": config["IGDB_API"]["client_secret"],
        "grant_type": "client_credentials"
    }
    response = requests.post("https://id.twitch.tv/oauth2/token", params=params)
    data = response.json()
    return data
