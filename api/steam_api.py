import requests

def get_url(BASE_URL, end_point):

    url = BASE_URL+f'/{end_point}'

    return url

def get_owned_games(BASE_URL, end_point, key, steam_id):

    url = get_url(BASE_URL, end_point)

    url = url+f'?key={key}&steamid={steam_id}&format=json'

    r = requests.get(url)

    game_list = []

    for i in (r.json()['response']['games']):  
        games = i['appid']
        game_list.append(games)

    return game_list