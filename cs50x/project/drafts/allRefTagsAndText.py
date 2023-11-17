import xml.etree.ElementTree as ET
from flask import Flask

# Parse XML document as tree and root
tree = ET.parse('PnPshort.xml')
root = tree.getroot()

# Iterate through document, looking through instances of spoken language indicated by "ref"
for i in root.iter(tag="{http://www.tei-c.org/ns/1.0}ref"):

  # Add inner text mentioned between ref tags to document
  innerText = ''.join(i.itertext())

  # Print inner text and separate each instance with "ref" tag
  print(i.tag, innerText)

