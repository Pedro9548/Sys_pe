import requests
import re
from bs4 import BeautifulSoup

def remover_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def regex_cleaner(clean_string, app_id):

    regex_memory = re.search(r'(Memory).*?(\d+.*?GB)', clean_string)
    regex_processor = re.search(r"(Processor)\s*(.*?)\s*(?=[A-Z]\w*:)", clean_string)
    regex_graphics = re.search(r"(Graphics)\s*(.*?)\s*(?=[A-Z]\w*:)", clean_string)

    regex_storage = re.search(r"(Storage)\s*(.*?(?<=[a-z]))(?=[A-Z])", clean_string)
    if regex_storage is None:
        regex_storage = re.search(r"(Hard Drive)\s*(.*?(?<=[a-z]))(?=[A-Z])", clean_string)

    # print(regex_storage)

    result_memory = regex_memory.group(1,2)
    result_processor = regex_processor.group(1,2)
    result_graphics = regex_graphics.group(1,2)
    result_storage = regex_storage.group(1, 2)

    clean_dict = {
        'app_id': str(f'{app_id}'),
        result_memory[0]: result_memory[1],
        result_processor[0]: result_processor[1],
        result_graphics[0]: result_graphics[1],
        result_storage[0]: result_storage[1]
    }

    return clean_dict


def get_app_details(app_id):

    URL_BASE = f'https://store.steampowered.com/api/appdetails?appids={app_id}'

    r = requests.get(URL_BASE)

    try:
        minimum_req = r.json()[f'{app_id}']['data'].get('pc_requirements', None)['minimum']
    except:
        print(f"ID: {app_id} não foi encontrado")

    clean_string = remover_html(minimum_req)

    # print(clean_string)

    regex_dict = regex_cleaner(clean_string, app_id)

    return regex_dict

