import json
from time import sleep

submissions = 0
#ships = {}

def separate(l, k):
  for i in range(len(k)):
    if k[i] in l:
      r = k[i]
      l.remove[r]

while True:         #try a counter variable, stops after 4 ships saved? saves each submitted to a different integer key?
  with open('web.txt', 'r') as f:
    data = json.load(f)
  
  if data["submitted"] == "Submit": # IF SUBMITTED, UPDATE SHIP, IF NOT  make ships empty (how to separate/save different ships?)
    submissions += 1

    if submissions == 1:
      #ships["Battleship"] = data["Coordinates"]
      Battleship = data["Coordinates"]

    elif submissions == 2:
      #ships["Submarine 1"] = data["Coordinates"]
      Submarine1 = data["Coordinates"]
    elif submissions == 3:
      #ships["Submarine 2"] = data["Coordinates"]
      Submarine2 = data["Coordinates"]

    elif submissions == 4:
      #ships["Destroyer"] = data["Coordinates"]
      Destroyer = data["Coordinates"]


    #ships["ship"] = data["Coordinates"]
  #else: 
    #ships["ship"] = " "

  print(ships)

  data2send = {"Coordinates":" ", "submitted":" "}
  with open('web.txt', 'w') as f:
    json.dump(data2send,f)
  sleep(0.1)

  if submissions > 3:
    break

separate(Battleship, Submarine1)
separate(Submarine1, Submarine2)
separate(Submarine2, Destroyer)

print("All ships selected")
print(Battleship)
print(Submarine1)
print(Submarine2)
print(Destroyer)
# if len = 4: save [0-3] as battleship
# if len = 7: save new coords as submarine
# if len = 10: save new coords as submarine
# if len = 12: save new coords as destroyer