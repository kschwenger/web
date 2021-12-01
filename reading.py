import json
from time import sleep

submissions = 0
#ships = {}

def separate(k, l):     # remove any coordinate from new ship if its in old ship
  for i in range(len(k)):
    if k[i] in l:
      l.remove(k[i])

def sepall():           # separate all ship coordinates
  separate(Battleship, Submarine1)
  separate(Battleship, Submarine2)
  separate(Battleship, Destroyer)
  separate(Submarine1, Submarine2)
  separate(Submarine1, Destroyer)
  separate(Submarine2, Destroyer)

while True:
  # read txt file
  with open('web.txt', 'r') as f:
    data = json.load(f)
  
  # update ships if user has clicked Submit
  if data["submitted"] == "Submit":
    submissions += 1

    # update Battleship coords
    if submissions == 1:
      #ships["Battleship"] = data["Coordinates"]
      Battleship = data["Coordinates"]
    # update Sub1 coords
    elif submissions == 2:
      #ships["Submarine 1"] = data["Coordinates"]
      Submarine1 = data["Coordinates"]
    # update Sub2 coords
    elif submissions == 3:
      #ships["Submarine 2"] = data["Coordinates"]
      Submarine2 = data["Coordinates"]
    #update Destroyer coords
    elif submissions == 4:
      #ships["Destroyer"] = data["Coordinates"]
      Destroyer = data["Coordinates"]
  
  # send blank to txt file
  data2send = {"Coordinates":" ", "submitted":" "}
  with open('web.txt', 'w') as f:
    json.dump(data2send,f)
  sleep(0.1)

  # stop loop after all ships submitted
  if submissions > 3:
    break

sepall()

print("All ships placed")
print("Battleship coordinates: "
print(Battleship)
print("Submarine 1 coordinates: "
print(Submarine1)
print("Submarine 2 coordinates: "
print(Submarine2)
print("Destroyer coordinates: "
print(Destroyer)