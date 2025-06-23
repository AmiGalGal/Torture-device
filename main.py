import requests
import time
import os

API_KEY = 'STEAM-API-KEY'
STEAM_ID64 = 'Friends steam id the 64 bit one'
ELDEN_RING_APPID = '1245620' #game id

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def is_playing_elden_ring():
    url = (
        f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
        f'?key={API_KEY}&steamids={STEAM_ID64}'
    )

    retry_backoff = 60
    max_backoff = 300

    for attempt in range(5):
        try:
            response = requests.get(url, headers=HEADERS)

            if response.status_code == 429:
                print(f"Rate limit hit. Waiting {retry_backoff} seconds")
                time.sleep(retry_backoff)
                retry_backoff = min(retry_backoff * 2, max_backoff)
                continue

            elif response.status_code != 200:
                print(f"HTTP error: {response.status_code}")
                return False

            data = response.json()
            player = data['response']['players'][0]
            game_id = player.get('gameid', '')
            return game_id == ELDEN_RING_APPID

        except (KeyError, IndexError):
            print("nigga offline")
            return False

        except Exception as e:
            print("nigga is error", e)
            time.sleep(60)
            continue

    print("nigga failed")
    return False

while True:
    if is_playing_elden_ring():
        print("nigga in the house")
        os.startfile("24f7316f62873c6b.mp4") #ear rape :(
        break
    else:
        print("nigga not in the house")
        time.sleep(90)
