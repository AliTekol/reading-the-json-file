import json

with open('games.json', 'r') as f:
   gamelist = json.load(f)

for game in gamelist['games']:
    print(game['name'])