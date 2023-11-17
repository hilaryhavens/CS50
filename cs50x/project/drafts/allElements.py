import xml.etree.ElementTree as ET
from flask import Flask

tree = ET.parse('PnPshort.xml')
root = tree.getroot()
for q in root.findall(".//{http://www.tei-c.org/ns/1.0}seg"):
    print(q)

