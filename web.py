#!/usr/bin/python37all

import cgi
import cgitb # see next line
cgitb.enable() # exception handler, displays uncaught errors
import json
from urllib.request import urlopen # use to send/receive data
from urllib.parse import urlencode # use to structure a GET string

# global variables 
AllCoords = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']
count = 0

# get data from html form
dataFromhtml = cgi.FieldStorage()
Coordinates = dataFromhtml.getvalue('option') # save chosen coordinates as a list

def checking(coord): # check each coord to see if already picked, display as checked if so
  global count
  if isinstance(Coordinates, list):
    if Coordinates.count(coord) > 0:
      print('<input type="checkbox" name="option" value="%s" checked>' % coord)
    else:
      print('<input type="checkbox" name="option" value="%s">' % coord)
  elif isinstance(Coordinates, str):
    if Coordinates == coord:
      print('<input type="checkbox" name="option" value="%s" checked>' % coord)
    else:
      print('<input type="checkbox" name="option" value="%s">' % coord)
  else:
    print('<input type="checkbox" name="option" value="%s">' % coord)
  
  count += 1
  if count >= 8: 
    print('<br>')
    count = 0


# html code
print('Content-type: text/html\n\n')
print('<html>')

# make sure something is selected, print the coordinates list (or singular coordinate)

print('<h1>BATTLESHIP</h1>')

if isinstance(Coordinates, list):
  print('Previous Selections: ')
  for i in range(len(Coordinates)):
    print('  ' + Coordinates[i])
elif isinstance(Coordinates, str):
  print('Previous Selections: ' + Coordinates)
else:
  print('No selection, select again')

# rest is the same as html for now
print('<br>')
print('Place Ships <br>')
print('<form action="/cgi-bin/web.py" method="POST">')

for elem in AllCoords:
  checking(elem)

print('<input type="submit" value="Submit">')

print('</form>')


# grid display
print("""
<head>
<style>
.grid-container {
display: grid;
grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
aspect-ratio: 1;
height: 400px;
width: 400px;
}
.grid-item {
background-color: rgba(255, 255, 255, 0.8);
border: 1px solid rgba(0, 0, 0, 0.8);
padding: 15px;
font-size: 20px;
text-align: center;
}
</style>
</head>
<body>

<div class="grid-container">

""")
#update 
for elem in AllCoords:
  if isinstance(Coordinates, list):
    if Coordinates.count(elem) > 0:
      print('<div class="grid-item">x</div>')
    else:
      print('<div class="grid-item"> </div>')
  elif isinstance(Coordinates, str):
    if Coordinates == elem:
      print('<div class="grid-item">x</div>')
    else:
      print('<div class="grid-item"> </div>')
  else:
    print('<div class="grid-item"> </div>')
print('</body>')
print('</html>')