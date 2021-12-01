import json

ships = {}

while True:
  with open('web.txt', 'r') as f:
    data = json.load(f)
  
  ships["destroyer"] = data

  print(ships["destroyer"])