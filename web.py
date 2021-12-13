#!/usr/bin/python37all

import cgi
import cgitb 
cgitb.enable() # exception handler, displays uncaught errors
import json
from urllib.request import urlopen # use to send/receive data
from urllib.parse import urlencode # use to structure a GET string

# global variables 
# for checkboxes and grid display
AllCoords = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']
Rowdict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8} # for sorting and validating ships
Completed = False # True once all ships placed


def IsItValid(ship):  # Returns true if all coordinates are adjacent in same row/column
  Valid = True
  for coordinate in range(len(ship)-1):
    if ship[0][0] == ship[coordinate+1][0] and ship[0][0] == ship[-1][0]: # if coordinates have same letter (row)
      if abs(int(ship[coordinate][1]) - int(ship[coordinate+1][1])) > 1: # if coordinate numbers (columns) not adjacent
        Valid = False
        break
      else:
        pass
    elif ship[0][1] == ship[coordinate+1][1] and ship[0][1] == ship[-1][1]: # if coordinates have same number (column)
      if abs(Rowdict[ship[coordinate][0]] - Rowdict[ship[coordinate+1][0]]) > 1: # if coordinate letters (rows) not adjacent
        Valid = False
        break
      else:
        pass
    else:
      Valid = False
      break
  return Valid

def separate(old, new):     # remove any coordinate from new ship if it is in old ship, return as new ship
  ship = [x for x in new if x not in old]
  return ship

# html content type and style classes in CSS, all for html page design and grid container
print('Content-type: text/html\n\n')
print('<html>')
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
  width:1000px;
}
body {
  background-image: url('https://images.theconversation.com/files/295442/original/file-20191003-52796-1763ajl.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=675.0&fit=crop');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
</head>
<img src="https://i.ibb.co/CKMGM49/Battleship-Logo.png" alt="Battleship Logo" class="centimg">
""")

# get data from html form
dataFromhtml = cgi.FieldStorage()
Coordinates = dataFromhtml.getvalue('option') # save chosen coordinates as a list
Submit = dataFromhtml.getvalue('submitted')

print('<body>') # start body of html page
print('<h2 style="text-align:center;">')

if isinstance(Coordinates, list): # if Coordinates is a list (>1 total boxes checked)
  
  if len(Coordinates) > 3: # if more than 3 boxes checked
    
    if len(Coordinates) == 4:
      if IsItValid(Coordinates) == True:  # check validity 
        with open('SaveCoords.txt', 'w') as f:  # save total coords to separate ships later, save Battleship for main code
          json.dump({"TotalCoords":Coordinates, "Battleship":Coordinates},f)
        print('Place <span style="color:OrangeRed"> Submarine </span> (3 coordinates) <br>')
      else:
        Coordinates = []  # save blank list in order to display blank grid
        print('Invalid selection.  Place <span style="color:OrangeRed"> Battleship </span> (4 coordinates next to each other in a single row or column) <br>')
  
    elif len(Coordinates) == 7:
      with open('SaveCoords.txt', 'r') as f:  # load the saved coordinates from last submission
        ships = json.load(f)
      Submarine = separate(ships["TotalCoords"], Coordinates) # separate new ship submission from previous submitted coords
      if IsItValid(Submarine) == True:
        with open('SaveCoords.txt', 'w') as f:  # save ships and total coordinates
          json.dump({"TotalCoords":Coordinates, "Battleship":ships["Battleship"], "Submarine":Submarine},f)
        print('Place <span style="color:OrangeRed"> Cruiser </span> (3 coordinates) <br>')
      else:
        Coordinates = ships["TotalCoords"]  # reset saved coordinates to most recent valid submission
        print('Invalid selection. Place <span style="color:OrangeRed"> Submarine </span> (3 coordinates next to each other in a single row or column) <br>')

    elif len(Coordinates) == 10:  # same as above
      with open('SaveCoords.txt', 'r') as f:
        ships = json.load(f)
      Cruiser = separate(ships["TotalCoords"], Coordinates)
      if IsItValid(Cruiser) == True:
        with open('SaveCoords.txt', 'w') as f:
          json.dump({"TotalCoords":Coordinates, "Battleship":ships["Battleship"], "Submarine":ships["Submarine"], "Cruiser":Cruiser},f)
        print('Place <span style="color:OrangeRed"> Destroyer </span> (2 coordinates) <br>')
      else:
        Coordinates = ships["TotalCoords"]
        print('Invalid selection. Place <span style="color:OrangeRed"> Cruiser </span> (3 coordinates next to each other in a single row or column) <br>')
  
    elif len(Coordinates) == 12:  # same as above
      with open('SaveCoords.txt', 'r') as f:
        ships = json.load(f)
      Destroyer = separate(ships["TotalCoords"], Coordinates)
      if IsItValid(Destroyer) == True:
        with open('SaveCoords.txt', 'w') as f:
          json.dump({"TotalCoords":Coordinates, "Battleship":ships["Battleship"], "Submarine":ships["Submarine"], "Cruiser":ships["Cruiser"], "Destroyer":Destroyer, "submitted":Submit},f)
        print('All ships placed <br>')
        Completed = True  # mark as true to remove submit button
      else:
        Coordinates = ships["TotalCoords"]
        print('Invalid selection. Place <span style="color:OrangeRed"> Destroyer </span> (2 coordinates next to each other in a single row or column) <br>')
  
    else: # if Coordinates is not length 4, 7, 10, or 12
      with open('SaveCoords.txt', 'r') as f:  # load saved coordinates
        ships = json.load(f)
      Coordinates = ships["TotalCoords"]  # reset coordinates to most recent valid submission
      if "Cruiser" in ships:              # request next ship depending on which ships have been saved
        print('Invalid selection.  Place <span style="color:OrangeRed"> Destroyer </span> (2 coordinates next to each other in a single row or column) <br>')
      elif "Submarine" in ships:
        print('Invalid selection.  Place <span style="color:OrangeRed"> Cruiser </span> (3 coordinates next to each other in a single row or column) <br>')
      elif "Battleship" in ships:
        print('Invalid selection.  Place <span style="color:OrangeRed"> Submarine </span> (3 coordinates next to each other in a single row or column) <br>')
      else:
        print('Invalid selection.  Place <span style="color:OrangeRed"> Battleship </span> (4 coordinates next to each other in a single row or column) <br>')

  else: # if Coordinates is length 2 or 3 (2 or 3 total boxes checked)
    Coordinates = []  # set coordinates as empty for blank grid
    print('Invalid selection.  Place <span style="color:OrangeRed"> Battleship </span> (4 coordinates next to each other in a single row or column) <br>')

else: # if Coordinates is not a list (0 or 1 total boxes checked)
  Coordinates = []  # set coordinates as empty for blank grid
  print('Invalid selection, Place <span style="color:OrangeRed"> Battleship </span> (4 coordinates next to each other in a single row or column) <br>')
print('</h2>')

# start checkbox form, each checkbox goes into the grid container as a grid item
print('<form class="center" action="/cgi-bin/web.py" method="POST">')
print('<h3 class="center">')

# update grid display
print('<div class="grid-container">')
print('<div class="grid-itemBlank"> </div>')
for i in range(8):  # print column labels (numbers)
  print('<div class="grid-itemBlank"> %s </div>' %str(i+1))
print('<div class="grid-itemBlank"> A </div>')  # print first row label "A"
counter = 0
rowletter = 1
for elem in AllCoords:
  if Coordinates.count(elem) > 0: # if the coordinate has been saved, mark it as checked
    print('<div class="grid-itemFill"> <input type="checkbox" name="option" value="%s" checked> </span> </div>' %elem)
  else:
    print('<div class="grid-itemEmpt"> <input type="checkbox" name="option" value="%s"> </div>' %elem)
  counter += 1
  if counter >= 8:  # start a new row
    counter = 0
    if rowletter < 8: # print the row labels (numbers)
      print('<div class="grid-itemBlank"> %s </div>' %list(Rowdict.keys())[rowletter])
      rowletter += 1
print('</div>')
print('<br>')
print('<br>')
print('<br>')

if Completed == True: # only include submit button if all ships have been placed
  pass
else:
  print('<input type="submit" name="submitted" value="Submit" style="height:60px; width:120px">')

print('</h3>')
print('</form>')
print('</body>')
print('</html>') # closing html things

# Kevin Schwenger, Chris Jean-Rene, Kyle Shreve
# ENME441 Course Project
# Professor DeVoe
# Last Update: 12/12/2021 7:17PM