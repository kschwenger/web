import json
from time import sleep

with open('SaveCoords.txt', 'r') as f:
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

with open('SaveCoords.txt', 'w') as f:
  json.dump({"TotalCoords":[]},f)

#12/4 4:25pm