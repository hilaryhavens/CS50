import xml.etree.ElementTree as ET
from flask import Flask

# Parse XML document as tree and root
tree = ET.parse('PnPshort.xml')
root = tree.getroot()

# Iterate through document, looking through instances of spoken language indicated by "ref"
for i in root.iter(tag="{http://www.tei-c.org/ns/1.0}ref"):
  for j in i.iter(tag="{http://www.tei-c.org/ns/1.0}said"):
    who = j.get('who')
    # The commented out print line shows the full tags and attributes for checking
    #print(i.tag, j.tag, j.attrib)
    print(who)


