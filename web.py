#!/usr/bin/python37all

import cgi
import cgitb # see next line
cgitb.enable() # exception handler, displays uncaught errors
import json
from urllib.request import urlopen # use to send/receive data
from urllib.parse import urlencode # use to structure a GET string

# get data from html form
dataFromhtml = cgi.FieldStorage()
Coordinates = dataFromhtml.getvalue('option') # save chosen coordinates as a list

# html code
print('Content-type: text/html\n\n')
print('<html>')

# make sure something is selcted, print the coordinates list 
if isinstance(Coordinates, list):
  print('Previous Selections: ')
  for i in range(len(Coordinates)):
    print('  ' + Coordinates[i])
else:
  print('No selection, select again')

# grid display
print("""
<head>
<style>
.grid-container {
display: grid;
grid-template-columns: auto auto auto auto auto auto auto auto;
background-color: #2196F3;
padding: 10px;
}
.grid-item {
background-color: rgba(255, 255, 255, 0.8);
border: 1px solid rgba(0, 0, 0, 0.8);
padding: 20px;
font-size: 30px;
text-align: center;
}
</style>
</head>
<body>

<h1>Grid Elements</h1>

<p>A Grid Layout must have a parent element with the <em>display</em> property set to <em>grid</em> or <em>inline-grid</em>.</p>

<p>Direct child element(s) of the grid container automatically becomes grid items.</p>

<div class="grid-container">
<div class="grid-item">1</div>
<div class="grid-item">2</div>
<div class="grid-item">3</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">1</div>
<div class="grid-item">2
</div>

</body>
""")

# rest is the same as html for now
print('<br>')
print('Place Ships <br>')
print('<form action="/cgi-bin/web.py" method="POST">')
print('<input type="checkbox" name="option" value="A1">')
print('<input type="checkbox" name="option" value="A2">')
print('<input type="checkbox" name="option" value="A3">')
print('<input type="checkbox" name="option" value="A4">')
print('<input type="checkbox" name="option" value="A5">')
print('<input type="checkbox" name="option" value="A6">')
print('<input type="checkbox" name="option" value="A7">')
print('<input type="checkbox" name="option" value="A8">')
print('<br>')
print('<input type="checkbox" name="option" value="B1">')
print('<input type="checkbox" name="option" value="B2">')
print('<input type="checkbox" name="option" value="B3">')
print('<input type="checkbox" name="option" value="B4">')
print('<input type="checkbox" name="option" value="B5">')
print('<input type="checkbox" name="option" value="B6">')
print('<input type="checkbox" name="option" value="B7">')
print('<input type="checkbox" name="option" value="B8">')
print('<br>')
print('<input type="checkbox" name="option" value="C1">')
print('<input type="checkbox" name="option" value="C2">')
print('<input type="checkbox" name="option" value="C3">')
print('<input type="checkbox" name="option" value="C4">')
print('<input type="checkbox" name="option" value="C5">')
print('<input type="checkbox" name="option" value="C6">')
print('<input type="checkbox" name="option" value="C7">')
print('<input type="checkbox" name="option" value="C8">')
print('<br>')
print('<input type="checkbox" name="option" value="D1">')
print('<input type="checkbox" name="option" value="D2">')
print('<input type="checkbox" name="option" value="D3">')
print('<input type="checkbox" name="option" value="D4">')
print('<input type="checkbox" name="option" value="D5">')
print('<input type="checkbox" name="option" value="D6">')
print('<input type="checkbox" name="option" value="D7">')
print('<input type="checkbox" name="option" value="D8">')
print('<br>')
print('<input type="checkbox" name="option" value="E1">')
print('<input type="checkbox" name="option" value="E2">')
print('<input type="checkbox" name="option" value="E3">')
print('<input type="checkbox" name="option" value="E4">')
print('<input type="checkbox" name="option" value="E5">')
print('<input type="checkbox" name="option" value="E6">')
print('<input type="checkbox" name="option" value="E7">')
print('<input type="checkbox" name="option" value="E8">')
print('<br>')
print('<input type="checkbox" name="option" value="F1">')
print('<input type="checkbox" name="option" value="F2">')
print('<input type="checkbox" name="option" value="F3">')
print('<input type="checkbox" name="option" value="F4">')
print('<input type="checkbox" name="option" value="F5">')
print('<input type="checkbox" name="option" value="F6">')
print('<input type="checkbox" name="option" value="F7">')
print('<input type="checkbox" name="option" value="F8">')
print('<br>')
print('<input type="checkbox" name="option" value="G1">')
print('<input type="checkbox" name="option" value="G2">')
print('<input type="checkbox" name="option" value="G3">')
print('<input type="checkbox" name="option" value="G4">')
print('<input type="checkbox" name="option" value="G5">')
print('<input type="checkbox" name="option" value="G6">')
print('<input type="checkbox" name="option" value="G7">')
print('<input type="checkbox" name="option" value="G8">')
print('<br>')
print('<input type="checkbox" name="option" value="H1">')
print('<input type="checkbox" name="option" value="H2">')
print('<input type="checkbox" name="option" value="H3">')
print('<input type="checkbox" name="option" value="H4">')
print('<input type="checkbox" name="option" value="H5">')
print('<input type="checkbox" name="option" value="H6">')
print('<input type="checkbox" name="option" value="H7">')
print('<input type="checkbox" name="option" value="H8">')
print('<br>')

print('<input type="submit" value="Submit">')

print('</form>')
print('</html>')