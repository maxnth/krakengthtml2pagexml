import src.utils as utils
from src.PAGEXML.builder import PAGEBuilder

from pathlib import Path
import base64


class Converter:
    def __init__(self, file: Path, out_filename, out="."):
        self.filename = file.stem
        self.out = out
        self.out_filename = out_filename
        self.tree = utils.parse_file(str(file))
        self.xml = PAGEBuilder(tree=self.tree, filename=self.out_filename)

    def build(self):
        self.xml.build()

    def export_image(self):
        with open(Path(self.out, self.out_filename).with_suffix(".png"), "wb") as image_file:
            image_file.write(base64.decodebytes(self.xml.image["base64"]))

    def export_xml(self):
        with open(Path(self.out, self.out_filename).with_suffix(".xml"), "w") as xml_file:
            xml_file.write(str(self.xml))

    def export(self):
        self.build()

        self.export_image()
        self.export_xml()
