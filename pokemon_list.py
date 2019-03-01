#获取完整的精灵列表

import requests
from pokemonGo import pokemon_db as db

list_url = 'https://cn.portal-pokemon.com/play/pokedex/api/v1'
headers = {
    'Referer': 'https://cn.portal-pokemon.com/play/pokedex',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
params = {
    'pokemon_ability_id': '',
    'zukan_id_from': 1,
    'zukan_id_to': 807
}


def get_pokemon_list():
    try:
        r = requests.get(list_url, params=params, headers=headers)
        r.raise_for_status()
        print(r.status_code)
        r.encoding = "utf-8"
        print("=" * 10)
        result = r.json()
        if db.insert_list(result["pokemons"]):
            print("插入数据库成功")
    except requests.exceptions.RequestException as e:
        print("Error: ", e)


def main():
    print(__name__)
    get_pokemon_list()


if __name__ == "__main__":
    main()
