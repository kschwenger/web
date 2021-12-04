import json
from time import sleep

submissions = 0
Rowdict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8} # for sorting and validating purposes
#ships = {}

def separate(old, new):     # remove any coordinate from new ship k if they are in old ship l
  for i in range(len(old)):
    if old[i] in new:
      new.remove(old[i])

def sepall():           # separate all ship coordinates
  separate(Battleship, Submarine)
  separate(Battleship, Cruiser)
  separate(Battleship, Destroyer)
  separate(Submarine, Cruiser)
  separate(Submarine, Destroyer)
  separate(Cruiser, Destroyer)

def IsItValid(ship):  # are they next to each other
  for coordinate in range(len(ship)-1):
    if ship[coordinate][0] == ship[coordinate+1][0]:
      if abs(int(ship[coordinate][1]) - int(ship[coordinate+1][1])) > 1:
        print("%s is invalid!" % ship)
        break
      else:
        pass
    elif ship[coordinate][1] == ship[coordinate+1][1]:
      if abs(Rowdict[ship[coordinate][0]] - Rowdict[ship[coordinate+1][0]]) > 1:
        print("%s is invalid!!" % ship)
        break
      else:
        pass
    else:
      print("%s is invalid!!!" % ship)
      break

def AreAllValid():  #check if all ships are valid
  IsItValid(Battleship)
  IsItValid(Submarine)
  IsItValid(Cruiser)
  IsItValid(Destroyer)  

"""
while True:
  # read txt file
  with open('web.txt', 'r') as f:
    ships = json.load(f)
  
  # update ships if user has clicked Submit
  if ships["submitted"] == "Submit":
    submissions += 1

    # update Battleship coords
    if submissions == 1:
      #ships["Battleship"] = data["Coordinates"]
      Battleship = ships["Battleship"]
    # update Sub1 coords
    elif submissions == 2:
      #ships["Submarine 1"] = data["Coordinates"]
      Submarine = ships["Submarine"]
    # update Sub2 coords
    elif submissions == 3:
      #ships["Submarine 2"] = data["Coordinates"]
      Cruiser = ships["Cruiser"]
    #update Destroyer coords
    elif submissions == 4:
      #ships["Destroyer"] = data["Coordinates"]
      Destroyer = ships["Destroyer"]
  
  # send blank to txt file
  data2send = {"Coordinates":" ", "submitted":" "}
  with open('web.txt', 'w') as f:
    json.dump(data2send,f)
  sleep(0.1)

  # stop loop after all ships submitted
  if submissions > 3:
    break
"""
#sepall()

with open('web.txt', 'r') as f:
  ships = json.load(f)
Battleship = ships["Battleship"]
Submarine = ships["Submarine"]
Cruiser = ships["Cruiser"]
Destroyer = ships["Destroyer"]


print("All ships placed")
print("Battleship coordinates: ")
print(Battleship)
print("Submarine coordinates: ")
print(Submarine)
print("Cruiser coordinates: ")
print(Cruiser)
print("Destroyer coordinates: ")
print(Destroyer)

#AreAllValid()