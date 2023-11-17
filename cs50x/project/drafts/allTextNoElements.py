import xml.etree.ElementTree as ET
from flask import Flask

tree = ET.parse('PnPshort.xml')
root = tree.getroot()
print(''.join(root.itertext()))