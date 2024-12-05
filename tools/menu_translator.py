import xml.etree.ElementTree as ET
import csv

root = ET.parse("menu.xml").getroot()
ns = {'': 'http://openbox.org/', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
ET.register_namespace('', "http://openbox.org/")

# csv English, German
with open("translate.csv", "r") as f:
    csvFile =csv.reader(f)
    for lines in csvFile:
        print(lines[0], lines[1])

        for item in root.findall('.//{*}menu', ns):
            for m in item.iter():
                if m.tag == "{http://openbox.org/}item":
                    if m.get('label') == lines[0]:
                        m.set("label",lines[1].lstrip())

# Pretty Print and write to file
print()
tree = ET.ElementTree(root)
ET.indent(tree, space="  ")
tree.write("menu_de.xml", xml_declaration=True, encoding="utf-8")

ET.dump(root)
