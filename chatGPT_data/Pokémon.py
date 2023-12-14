import requests
# ポケモンの情報を取得する関数
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        return None
# ポケモンの情報を表示する関数
def display_pokemon_info(pokemon_data):
    if pokemon_data:
        print("ポケモン名:", pokemon_data["name"])
        print("高さ:", pokemon_data["height"])
        print("重さ:", pokemon_data["weight"])
        print("タイプ:")
        for type_data in pokemon_data["types"]:
            print("-", type_data["type"]["name"])
    else:
        print("ポケモンの情報を取得できませんでした。
# ポケモンの名前を入力して情報を取得する
pokemon_name = input("ポケモンの名前を入力してください: ")
pokemon_info = get_pokemon_info(pokemon_name)
display_pokemon_info(pokemon_info)
