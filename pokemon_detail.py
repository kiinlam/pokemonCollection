# 请求指定id的精灵页面，提取数据，写入数据库

import time
import random
import requests
from pokemonGo import pokemon_db as db
from pokemonGo import parse_page


detail_url = 'https://cn.portal-pokemon.com/play/pokedex/{}'
headers = {
    'Referer': 'https://cn.portal-pokemon.com/play/pokedex',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


def get_pokemon_detail(query_id):
    try:
        r = requests.get(detail_url.format(query_id), headers=headers)
        r.raise_for_status()
        print("请求编号：", query_id, r.status_code)
        return r.text
    except requests.exceptions.RequestException as e:
        print("Error: ", e)


def main():
    all_pokemon = db.find_all()

    for pokemon in all_pokemon:

        # 获取编号
        main_id = pokemon['zukan_id']
        sub_id = str(pokemon['zukan_sub_id'])

        if sub_id != '0':
            main_id += '_' + sub_id

        print("=" * 10)
        print('编号', main_id, pokemon['pokemon_name'], flush=True)

        # 请求网页
        res = get_pokemon_detail(main_id)

        # 解析网页
        parse_data = parse_page.parse(res)

        # 写入数据库
        db.update_detail(pokemon, parse_data)

        time.sleep(random.randint(3, 6))


if __name__ == "__main__":
    main()
