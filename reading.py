import json
from time import sleep

submissions = 0
#ships = {}

def separate(k, l):     # remove any coordinate from new ship if they are in old ship
  for i in range(len(k)):
    if k[i] in l:
      l.remove(k[i])

def sepall():           # separate all ship coordinates
  separate(Battleship, Submarine)
  separate(Battleship, Cruiser)
  separate(Battleship, Destroyer)
  separate(Submarine, Cruiser)
  separate(Submarine, Destroyer)
  separate(Cruiser, Destroyer)

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
      Submarine = data["Coordinates"]
    # update Sub2 coords
    elif submissions == 3:
      #ships["Submarine 2"] = data["Coordinates"]
      Cruiser = data["Coordinates"]
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
print("Battleship coordinates: ")
print(Battleship)
print("Submarine coordinates: ")
print(Submarine)
print("Cruiser coordinates: ")
print(Cruiser)
print("Destroyer coordinates: ")
print(Destroyer)

# are they next to each other
if Battleship[0][0] == Battleship[1][0]:  #if same letter
  if abs(Battleship[0][1] - Battleship[1][1]) > 1:
    print("invalid!")
  elif abs(Battleship[1][1] - Battleship[2][1]) > 1:
    print("invalid!!")
  elif abs(Battleship[2][1] - Battleship[3][1]) > 1:
    print("invalid!!!")
  else:
    print("Validdddd")