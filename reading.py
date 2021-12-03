import json
from time import sleep

submissions = 0
#ships = {}

def separate(k, l):     # remove any coordinate from new ship k if they are in old ship l
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


Rowdict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8} # for parsing purposes
# are they next to each other
if Battleship[0][0] == Battleship[1][0]:  #if first and second coord are same letter
  if Battleship[1][0] == Battleship[2][0]: #if second and third coord are same letter
    if Battleship[2][0] == Battleship[3][0]: #if third and fourth coord are same letter 
      if abs(int(Battleship[0][1]) - int(Battleship[1][1])) > 1: #if 1st and 2nd coord numbers are not next to each other
        print("invalid!")
      elif abs(int(Battleship[1][1]) - int(Battleship[2][1])) > 1:  #if 2nd and 3rd numbers are not next to each other
        print("invalid!!")
      elif abs(int(Battleship[2][1]) - int(Battleship[3][1])) > 1:  #if 3rd and 4th numbers are not next to each other
        print("invalid!!!")
      else:
        print("Validdddd")
    else:
      print("invalid!")
  else:
    print("invalid")
elif Battleship[0][1] == Battleship[1][1]:  #if first and second coord are same number 
  if Battleship[1][1] == Battleship[2][1]:  #if second and third coord are same number
    if Battleship[2][1] == Battleship[3][1]:  #if third and fourth coord are same number
      if abs(Rowdict[Battleship[0][0]] - Rowdict[Battleship[1][0]]) > 1:  #if number of letter of 1st and 2nd coords not next
        print("invalid")
      elif abs(Rowdict[Battleship[1][0]] - Rowdict[Battleship[2][0]]) > 1:
        print("invalid")
      elif abs(Rowdict[Battleship[2][0]] - Rowdict[Battleship[3][0]]) > 1:
        print("invalid")
      else:
        print("Valid")
    else:
      print("invalid")
  else:
    print("invalid")
else:
  print("innnnnnvalid")



