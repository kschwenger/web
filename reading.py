import json
from time import sleep

submissions = 0
Rowdict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8} # for sorting and validating purposes

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

def IsItValid(coords):  # are they next to each other
  Valid = True
  for coordinate in range(len(coords)-1):
    if coords[coordinate][0] == coords[coordinate+1][0]:
      if abs(int(coords[coordinate][1]) - int(coords[coordinate+1][1])) > 1:
        Valid = False
        break
      else:
        pass
    elif coords[coordinate][1] == coords[coordinate+1][1]:
      if abs(Rowdict[coords[coordinate][0]] - Rowdict[coords[coordinate+1][0]]) > 1:
        Valid =  False
        break
      else:
        pass
    else:
      Valid = False
      break
  return Valid

def AreAllValid():  #check if all ships are valid
  IsItValid(Battleship)
  IsItValid(Submarine)
  IsItValid(Cruiser)
  IsItValid(Destroyer)  

while True:
  # read txt file
  with open('web.txt', 'r') as f:
    data = json.load(f)
  
  # update ships if user has clicked Submit
  if data["submitted"] == "Submit":
    submissions += 1

    # update Battleship coords
    if submissions == 1:
      if IsItValid(data["Coordinates"]) == False:
        print("invalid")
        submissions -= 1
        #return something to cgi
        data2send = {"Coordinates":"invalid", "submitted":"invalid"}
        with open('web.txt', 'w') as f:
          json.dump(data2send,f)
      else:
        print("valid")
        Battleship = data["Coordinates"]

    # update Sub1 coords
    elif submissions == 2:
      Submarine = data["Coordinates"]
    # update Sub2 coords
    elif submissions == 3:
      Cruiser = data["Coordinates"]
    #update Destroyer coords
    elif submissions == 4:
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

AreAllValid()