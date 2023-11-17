import xml.etree.ElementTree as ET
from flask import Flask

tree = ET.parse('PnPshort.xml')
root = tree.getroot()
for i in root.iter(tag="{http://www.tei-c.org/ns/1.0}seg"):
  innerText = ''.join(i.itertext())
  print(i.tag, innerText)

