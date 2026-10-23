import xml.etree.ElementTree as ET
import re

# Parse the XML file and get the root element
xml = ET.parse("myfile.xml")
root = xml.getroot()

# Find the namespace dynamically using regular expressions
ns = re.match('{.*}', root.tag).group(0)

# Drill down to find specific elements (<edit-config>, <default-operation>, <test-option>)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))

# Print the values contained in the elements
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))# Fill in this file with the code from parsing XML exercise
