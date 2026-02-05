from api.steam_api import get_owned_games
from api.store_steam_api import get_app_details
from keys.key import api
import requests


BASE_URL = 'http://api.steampowered.com'
end_point = 'IPlayerService/GetOwnedGames/v0001/'

games = get_owned_games(BASE_URL=BASE_URL, end_point=end_point, key=api['api_key'], steam_id=api['steam_id'])

lista_result = []
lista_not_found = []

for i in games:
    try:
        lista_result.append((get_app_details(i)))
    except:
        lista_not_found.append(i)

print(lista_result)
print(lista_not_found)


