import json
from time import sleep

ships = {}

while True:
  with open('web.txt', 'r') as f:
    data = json.load(f)
  
  ships["ship"] = data["Coordinates"]

  print(ships["ship"])

  data2send = {"Coordinates":" "}
  with open('web.txt', 'w') as f:
    json.dump(data2send,f)
  
  sleep(0.1)
