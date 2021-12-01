import json
from time import sleep

ships = {}

while True:
  with open('web.txt', 'r') as f:
    data = json.load(f)
  
  if data["submitted"] == "Submit": # IF SUBMITTED, UPDATE SHIP, IF NOT DONT 
    ships["ship"] = data["Coordinates"]
  elif: 
    pass

  print(ships["ship"])

  data2send = {"Coordinates":" ", "submitted":" "}
  with open('web.txt', 'w') as f:
    json.dump(data2send,f)
  
  sleep(0.1)
