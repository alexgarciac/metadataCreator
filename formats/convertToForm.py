import re
import xmltodict

def get_namespace(element):
    m = re.match('\{.*\}', element.tag)
    return m.group(0) if m else ''

IN = "datacite-example-full-v4.0.xml"

with open(IN) as fd:
    root = xmltodict.parse(fd.read())
print()

def pretty(d, indent=0):
    if isinstance(d, dict):
        for key, value in d.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict) or isinstance(value, list):
                pretty(value, indent+1)
            else:
                listToEdit.append([key, value])
                print('\t' * (indent+1) + str(value))
    elif isinstance(d, list):
        for item in d:
            if isinstance(item, dict) or isinstance(item, list):
                pretty(item, indent+1)
            else:
                print('\t' * (indent+1) + str(item))
    else:
        pass


global listToEdit
listToEdit = []
pretty(root)
