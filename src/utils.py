from pathlib import Path
import io

import regex as re
from lxml import etree
from PIL import Image


def get_files(path=".", ext="html"):
    for file in sorted(Path(path).glob("*.{ext}".format(ext=ext))):
        yield file


def parse_file(doc):
    parser = etree.XMLParser(recover=True)
    return etree.parse(doc, parser)


def create_line_id(line_id):
    return "l{_lID}".format(_lID=line_id)


def format_bbox(x_min, y_min, x_max, y_max):
    return "{x_min},{y_max} {x_min},{y_min} {x_max},{y_min} {x_max},{y_max}".format(x_min=x_min, y_min=y_min,
                                                                                    x_max=x_max, y_max=y_max)


def calc_bbox(points):
    x_coordinates, y_coordinates = zip(*points)
    return min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates)


def create_line_dict(line):
    _text = "".join(line.itertext()).strip().replace("\t", "").replace("\n", "")

    return {"line_id": line.get("id"), "line_bbox": line.get("data-bbox"), "line_text": _text}


def get_img_base64(tree):
    full_base = tree.xpath("//img")[0].get("src").split(",")
    return "".join(re.findall("data:image/(.*);base64", full_base[0])), full_base[1]


def get_img_size(img):
    return Image.open(io.BytesIO(img)).size


def get_all_cords(elem):
    all_cords = list()
    lines = elem.xpath("//div[@class='column']/ul//li")
    for line in lines:
        coords = [int(coord) for coord in line.get("data-bbox").split(", ")]
        all_cords.extend([[coords[0], coords[1]], [coords[2], coords[3]]])
    return all_cords


def prettify(content):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(content, parser)
    return etree.tostring(tree, pretty_print=True)
