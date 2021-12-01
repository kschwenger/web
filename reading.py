import json
from time import sleep

submissions = 0
ships = {}

while True:         #try a counter variable, stops after 4 ships saved? saves each submitted to a different integer key?
  with open('web.txt', 'r') as f:
    data = json.load(f)
  
  if data["submitted"] == "Submit": # IF SUBMITTED, UPDATE SHIP, IF NOT  make ships empty (how to separate/save different ships?)
    submissions += 1
    ships["ship"] = data["Coordinates"]
  else: 
    ships["ship"] = " "

  print(ships["ship"])

  data2send = {"Coordinates":" ", "submitted":" "}
  with open('web.txt', 'w') as f:
    json.dump(data2send,f)
  sleep(0.1)

  if submissions > 3:
    break

print("All ships selected")
# if len = 4: save [0-3] as battleship
# if len = 7: save new coords as submarine
# if len = 10: save new coords as submarine
# if len = 12: save new coords as destroyer