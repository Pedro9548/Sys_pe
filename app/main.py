from api.steam_api import get_owned_games
from api.store_steam_api import get_app_details
from keys.key import api
import requests


BASE_URL = 'http://api.steampowered.com'
end_point = 'IPlayerService/GetOwnedGames/v0001/'

games = get_owned_games(BASE_URL=BASE_URL, end_point=end_point, key=api['api_key'], steam_id=api['steam_id'])

print(games)


