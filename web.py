#!/usr/bin/python37all

import cgi
import cgitb # see next line
cgitb.enable() # exception handler, displays uncaught errors
import json

print("""

Content-type: text/html\n\n
<html> 
Place Ships <br>
<form action="/cgi-bin/web.py" method="POST">
  <input type="checkbox" name="option" value="A1">
  <input type="checkbox" name="option" value="A2"> 
  <input type="checkbox" name="option" value="A3">
  <input type="checkbox" name="option" value="A4">
  <input type="checkbox" name="option" value="A5">
  <input type="checkbox" name="option" value="A6">
  <input type="checkbox" name="option" value="A7">
  <input type="checkbox" name="option" value="A8">
  <br>
  <input type="checkbox" name="option" value="B1">
  <input type="checkbox" name="option" value="B2"> 
  <input type="checkbox" name="option" value="B3">
  <input type="checkbox" name="option" value="B4">
  <input type="checkbox" name="option" value="B5">
  <input type="checkbox" name="option" value="B6">
  <input type="checkbox" name="option" value="B7">
  <input type="checkbox" name="option" value="B8"> 
  <br>
  <input type="checkbox" name="option" value="C1">
  <input type="checkbox" name="option" value="C2"> 
  <input type="checkbox" name="option" value="C3">
  <input type="checkbox" name="option" value="C4">
  <input type="checkbox" name="option" value="C5">
  <input type="checkbox" name="option" value="C6">
  <input type="checkbox" name="option" value="C7">
  <input type="checkbox" name="option" value="C8"> 
  <br>
  <input type="checkbox" name="option" value="C1">
  <input type="checkbox" name="option" value="C2"> 
  <input type="checkbox" name="option" value="C3">
  <input type="checkbox" name="option" value="C4">
  <input type="checkbox" name="option" value="C5">
  <input type="checkbox" name="option" value="C6">
  <input type="checkbox" name="option" value="C7">
  <input type="checkbox" name="option" value="C8"> 
  <br>
  <input type="checkbox" name="option" value="D1">
  <input type="checkbox" name="option" value="D2"> 
  <input type="checkbox" name="option" value="D3">
  <input type="checkbox" name="option" value="D4">
  <input type="checkbox" name="option" value="D5">
  <input type="checkbox" name="option" value="D6">
  <input type="checkbox" name="option" value="D7">
  <input type="checkbox" name="option" value="D8"> 
  <br>
  <input type="checkbox" name="option" value="E1">
  <input type="checkbox" name="option" value="E2"> 
  <input type="checkbox" name="option" value="E3">
  <input type="checkbox" name="option" value="E4">
  <input type="checkbox" name="option" value="E5">
  <input type="checkbox" name="option" value="E6">
  <input type="checkbox" name="option" value="E7">
  <input type="checkbox" name="option" value="E8"> 
  <br>
  <input type="checkbox" name="option" value="F1">
  <input type="checkbox" name="option" value="F2"> 
  <input type="checkbox" name="option" value="F3">
  <input type="checkbox" name="option" value="F4">
  <input type="checkbox" name="option" value="F5">
  <input type="checkbox" name="option" value="F6">
  <input type="checkbox" name="option" value="F7">
  <input type="checkbox" name="option" value="F8"> 
  <br>
  <input type="checkbox" name="option" value="G1">
  <input type="checkbox" name="option" value="G2"> 
  <input type="checkbox" name="option" value="G3">
  <input type="checkbox" name="option" value="G4">
  <input type="checkbox" name="option" value="G5">
  <input type="checkbox" name="option" value="G6">
  <input type="checkbox" name="option" value="G7">
  <input type="checkbox" name="option" value="G8"> 
  <br>
  <input type="checkbox" name="option" value="H1">
  <input type="checkbox" name="option" value="H2"> 
  <input type="checkbox" name="option" value="H3">
  <input type="checkbox" name="option" value="H4">
  <input type="checkbox" name="option" value="H5">
  <input type="checkbox" name="option" value="H6">
  <input type="checkbox" name="option" value="H7">
  <input type="checkbox" name="option" value="H8">  
  <br>
  <input type="submit" value="Submit">
  </form>
  </html>
  
""")