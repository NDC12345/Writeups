# xml_parse.py
from xml.etree import ElementTree, ElementInclude

xml = open("./data.xml", "r").read()
print("XPATH: ")
xpath = input()

try:
    res = ''
    root = ElementTree.fromstring(xml.strip())
    ElementInclude.include(root)
    for elem in root.findall(xpath):
        if elem.text != "":
            res += elem.text + ", "
    print('result:', res[:-2])
except Exception as e:
    print("Nani?")