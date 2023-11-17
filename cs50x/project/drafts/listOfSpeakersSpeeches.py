import xml.etree.ElementTree as ET
from flask import Flask

# Parse XML document as tree and root
tree = ET.parse('PnPshort.xml')
root = tree.getroot()

speeches = []

# Iterate through document, looking through instances of spoken language indicated by "ref"
for i in root.iter(tag="{http://www.tei-c.org/ns/1.0}ref"):

  # Iterate through those speeches to find who is speaking by printing the "who" attribute of the "said" tag
  for j in i.iter(tag="{http://www.tei-c.org/ns/1.0}said"):
    who = j.get('who')

  # Add inner text mentioned between ref tags to document
  innerText = ''.join(i.itertext())

  # Print speaker id and inner text
  speeches.append((who, innerText))

print(speeches)
