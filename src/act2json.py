
import argparse
import xml.etree.ElementTree as ET
import json
import glob
from clean import clean

parser = argparse.ArgumentParser(description='Convert Act XML files to JSONL')
parser.add_argument('-p', '--path', type=str, required=False, default='act/**/*.xml',
                    help='path to the files. accepts a glob pattern (e.g. act/**/*.xml)')
args = parser.parse_args()
files = glob.glob(args.path, recursive=True)

def to_txt(element):
    rc = ''
    if element is None or element.tag == 'preamble':
        return rc
    if element.text is not None:
        if element.tag == 'label':
            rc = "\n" + element.text.strip() + ": "
        elif element.tag == 'heading':
            rc = element.text.strip() + "\n"
        else:
            rc = element.text.strip() + " "

    for child in element:
        rc += " " + to_txt(child)

    return rc

# print(json.dumps(data, indent=4))
def convert(file):
    tree = ET.parse(file, ET.XMLParser(encoding='utf-8'))
    root = tree.getroot()
    j = dict()
    j['id'] = root.attrib['id']
    j['year'] = root.attrib['year']
    j['title'] = root.find('cover').find('title').text
    j['text'] = clean(to_txt(root.find('body')))
    with open(file.replace('.xml', '.json'), 'w') as f:
        f.write(json.dumps(j, indent=4))

for file in files:
    convert(file)