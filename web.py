#!/usr/bin/python37all

import cgi
import cgitb # see next line
cgitb.enable() # exception handler, displays uncaught errors
import json
from urllib.request import urlopen # use to send/receive data
from urllib.parse import urlencode # use to structure a GET string

# global variables 
# for checkboxes
AllCoords = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']
count = 0 # for checking function
Rowdict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8} # for sorting and validating purposes
Completed = False # True once all ships placed

def checking(coord): # check each coord to see if already picked, display as checked if so
  global count

  if isinstance(Coordinates, list):
    if Coordinates.count(coord) > 0:
      print('<input type="checkbox" name="option" value="%s" checked>' % coord)
    else:
      print('<input type="checkbox" name="option" value="%s">' % coord)
  
  else:
      print('<input type="checkbox" name="option" value="%s">' % coord)
  
  count += 1
  if count >= 8: 
    print('<br>')
    count = 0

def IsItValid(ship):  # are they next to each other
  Valid = True
  for coordinate in range(len(ship)-1):
    if ship[0][0] == ship[coordinate+1][0]:
      if abs(int(ship[coordinate][1]) - int(ship[coordinate+1][1])) > 1:
        Valid = False
        break
      else:
        pass
    elif ship[0][1] == ship[coordinate+1][1]:
      if abs(Rowdict[ship[coordinate][0]] - Rowdict[ship[coordinate+1][0]]) > 1:
        Valid = False
        break
      else:
        pass
    else:
      Valid = False
      break
  return Valid

def separate(old, new):     # remove any coordinate from new ship if it is in old ship
  ship = [x for x in new if x not in old]
  return ship

# html content type and style classes
print('Content-type: text/html\n\n')
print('<html style="background-color:DodgerBlue;">')
print("""
<head>
<style>
.grid-container {
display: grid;
grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
aspect-ratio: 1;
height: 450px;
width: 450px;
margin-left: auto;
margin-right: auto;
}
.grid-itemFill {
background-color: OrangeRed;
border: 1px solid rgba(0, 0, 0, 0.8);
padding: 15px;
font-size: 20px;
text-align: center;
}
.grid-itemEmpt {
background-color: White;
border: 1px solid rgba(0, 0, 0, 0.8);
padding: 15px;
font-size: 20px;
text-align: center;
}
.grid-itemBlank {
background-color: DarkGray;
border: 1px solid rgba(0, 0, 0, 0.8);
padding: 15px;
font-size: 20px;
text-align: center;
}
.center {
 text-align: center
}
.centimg {
  background-color: DodgerBlue;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width:600px;
  height:300px;
}

</style>
</head>
<body>
<img src="https://cloudfront-us-east-1.images.arcpublishing.com/ajc/GADQJXEQY5SCTPUAMTQGAHKT4U.jpg" alt="Battleship Logo" class="centimg">
""")

# get data from html form
dataFromhtml = cgi.FieldStorage()
Coordinates = dataFromhtml.getvalue('option') # save chosen coordinates as a list
Submit = dataFromhtml.getvalue('submitted')

print('<h2 style="text-align:center;">')

if isinstance(Coordinates, list): # if Coordinates is a list (>1 total boxes checked)

  if len(Coordinates) > 3: # if more than 3 boxes checked

    if len(Coordinates) == 4:
      if IsItValid(Coordinates) == True:
        with open('SaveCoords.txt', 'w') as f:
          json.dump({"TotalCoords":Coordinates, "Battleship":Coordinates},f)
        print('Place Submarine (3 coordinates) <br>')
      else:
        Coordinates = []
        print("Invalid selection.  Place Battleship (4 coordinates) <br>")
  
    elif len(Coordinates) == 7:
      with open('SaveCoords.txt', 'r') as f:
        ships = json.load(f)
      Submarine = separate(ships["TotalCoords"], Coordinates)
      if IsItValid(Submarine) == True:
        with open('SaveCoords.txt', 'w') as f:
          json.dump({"TotalCoords":Coordinates, "Battleship":ships["Battleship"], "Submarine":Submarine},f)
        print('Place Cruiser (3 coordinates) <br>')
      else:
        Coordinates = ships["TotalCoords"]
        print("Invalid selection. Place Submarine (3 coordinates) <br>")

    elif len(Coordinates) == 10:
      with open('SaveCoords.txt', 'r') as f:
        ships = json.load(f)
      Cruiser = separate(ships["TotalCoords"], Coordinates)
      if IsItValid(Cruiser) == True:
        with open('SaveCoords.txt', 'w') as f:
          json.dump({"TotalCoords":Coordinates, "Battleship":ships["Battleship"], "Submarine":ships["Submarine"], "Cruiser":Cruiser},f)
        print('Place Destroyer (2 coordinates) <br>')
      else:
        Coordinates = ships["TotalCoords"]
        print('Invalid selection. Place Cruiser (3 coordinates) <br>')
  
    elif len(Coordinates) == 12:
      with open('SaveCoords.txt', 'r') as f:
        ships = json.load(f)
      Destroyer = separate(ships["TotalCoords"], Coordinates)
      if IsItValid(Destroyer) == True:
        with open('SaveCoords.txt', 'w') as f:
          json.dump({"TotalCoords":Coordinates, "Battleship":ships["Battleship"], "Submarine":ships["Submarine"], "Cruiser":ships["Cruiser"], "Destroyer":Destroyer, "submitted":Submit},f)
        print('All ships placed <br>')
        Completed = True
      else:
        Coordinates = ships["TotalCoords"]
        print('Invalid selection. Place Destroyer (2 coordinates) <br>')
  
    else: # if Coordinates is not length 4, 7, 10, or 12
      with open('SaveCoords.txt', 'r') as f:
        ships = json.load(f)
      Coordinates = ships["TotalCoords"]
      if "Cruiser" in ships:
        print('Invalid selection.  Place Destroyer (2 coordinates) <br>')
      elif "Submarine" in ships:
        print('Invalid selection.  Place Cruiser (3 coordinates) <br>')
      elif "Battleship" in ships:
        print('Invalid selection.  Place Submarine (3 coordinates) <br>')
      else:
        print('Invalid selection.  Place Battleship (4 coordinates) <br>')

  else: # if Coordinates is length 2 or 3 (2 or 3total boxes checked)
    Coordinates = []
    print("Invalid selection.  Place Battleship (4 coordinates) <br>")

else: # if Coordinates is not a list (0 or 1 total boxes checked)
  Coordinates = []
  print('Invalid selection, Place Battleship (4 coordinates) <br>')

print('<form action="/cgi-bin/web.py" method="POST">')
print('</h2>')

print('<h3>')
# update grid display
print('<div class="grid-container">')
print('<div class="grid-itemBlank"> </div>')
for i in range(8):
  print('<div class="grid-itemBlank"> %s </div>' %str(i+1))
print('<div class="grid-itemBlank"> A </div>')
counter = 0
rowletter = 1
for elem in AllCoords:
  if Coordinates.count(elem) > 0:
    print('<div class="grid-itemFill"> <input type="checkbox" name="option" value="%s" checked> </span> </div>' %elem)
  else:
    print('<div class="grid-itemEmpt"> <input type="checkbox" name="option" value="%s"> </div>' %elem)
  counter += 1
  if counter >= 8:
    counter = 0
    if rowletter < 8:
      print('<div class="grid-itemBlank"> %s </div>' %list(Rowdict.keys())[rowletter])
      rowletter += 1

if Completed == True:
  pass
else:
  print('<input style="margin:auto;" type="submit" name="submitted" value="Submit">')
  
print('</form>')
print('</h3>')
print('</body>')
print('</html>') #close html page