import xml.etree.ElementTree as ET
from flask import Flask
import re

# Parse XML document as tree and root
tree = ET.parse('PnPshort.xml')
root = tree.getroot()

# Find ids
# Iterate through document, looking for character Ids
for i in root.iter(tag="{http://www.tei-c.org/ns/1.0}person"):

    # Extract ID attribute as part of list to avoid namespace issue
    ids = list(dict.values(i.attrib))[1]
    print(ids)
