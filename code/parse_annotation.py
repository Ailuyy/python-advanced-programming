import os
import xml.etree.ElementTree as ET

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..'))
annot_file = os.path.join(project_root, 'data', 'annotations.xml')

if not os.path.exists(annot_file):
    raise FileNotFoundError(f"No file: {annot_file}")

tree = ET.parse(annot_file)
root = tree.getroot()

def parse_annotation(filename: str):
    for image in root.findall('image'):
        name_attr = image.get('name')
        if name_attr == filename:
            box_elem = image.find('box')
            xtl = float(box_elem.get('xtl'))
            ytl = float(box_elem.get('ytl'))
            xbr = float(box_elem.get('xbr'))
            ybr = float(box_elem.get('ybr'))
            box = (int(xtl), int(ytl), int(xbr), int(ybr))
            text = ''
            for attr in box_elem.findall('attribute'):
                if attr.get('name') == 'plate number':
                    if attr.text:
                        text = attr.text.strip()
                    break
            return box, text
    raise ValueError(f"No annotations for file: {filename}")