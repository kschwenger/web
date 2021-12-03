#!/usr/bin/python37all

import time
import cgi
import cgitb # see next line
cgitb.enable() # exception handler, displays uncaught errors
import json
from urllib.request import urlopen # use to send/receive data
from urllib.parse import urlencode # use to structure a GET string

# global variables 
AllCoords = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']
count = 0

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

# html code
print('Content-type: text/html\n\n')
print('<html>')
print('<h1>BATTLESHIP</h1>')

# how to save a ship selection if the selction (after the fist) is invalid (how to not clear whole board, just the new invalid selection)?
# maybe send data only after correct number (4,7,10,12)
# do some validating within the main code and send back? can it be validated in cgi without saving?

# get data from html form
dataFromhtml = cgi.FieldStorage()
Coordinates = dataFromhtml.getvalue('option') # save chosen coordinates as a list
Submit = dataFromhtml.getvalue('submitted')

if isinstance(Coordinates, list):
  #do everything

  print('Previous Selections: ')
  for i in range(len(Coordinates)):
    print('  ' + Coordinates[i])
  print('<br>')

  # html stuff
  print('<br>')
  if len(Coordinates) == 4:
    # send data to json file
    data2send = {"Coordinates":Coordinates, "submitted":Submit}
    with open('web.txt', 'w') as f:
      json.dump(data2send,f)
    time.sleep(0.1)
    with open('web.txt', 'r') as f:
      backdata = json.load(f)
    if backdata["Coordinates"] == 1:
      print('Invalid Selection, select again')
      # do something else
    else:
      print('Place Submarine (3 coordinates) <br>')
  
  elif len(Coordinates) == 7:
    print('Place Cruiser (3 coordinates) <br>')
  elif len(Coordinates) == 10:
    print('Place Destroyer (2 coordinates) <br>')
  elif len(Coordinates) == 12:
    print('All ships placed <br>')
  else:
    print('Invalid selection, select again ')

  print('<form action="/cgi-bin/web.py" method="POST">')

  for elem in AllCoords:
    checking(elem)

  print('<input type="submit" name="submitted" value="Submit">')
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

  # update grid
  for elem in AllCoords:
    if Coordinates.count(elem) > 0:
      print('<div class="grid-item">x</div>')
    else:
      print('<div class="grid-item"> </div>')
    
  print('</body>')

else: #dont do everything, repick coordinates with same html
  print('Invalid selection, select again <br>')
  
  # send nothing to txt file
  data2send = {"Coordinates":" ", "submitted":" "}
  with open('web.txt', 'w') as f:
    json.dump(data2send,f)
  
  print('Place Ships <br>')
  print('<form action="/cgi-bin/web.py" method="POST">')

  for elem in AllCoords:
    checking(elem)

  print('<input type="submit" name="submitted" value="Submit">')
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

  # update grid
  for elem in AllCoords:
    print('<div class="grid-item"> </div>')
    
  print('</body>')

print('</html>')