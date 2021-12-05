import json
from time import sleep

while true:
  with open('SaveCoords.txt', 'r') as f:
    ships = json.load(f)
  if "Battlship" in ships:
    Battleship = ships["Battleship"]
  if "Submarine" in ships:
    Submarine = ships["Submarine"]
  if "Cruiser" in ships:
    Cruiser = ships["Cruiser"]
  if "Destroyer" in ships:
    Destroyer = ships["Destroyer"]
    break

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

