import src.utils as utils
from src.PAGEXML.builder import PAGEBuilder

from pathlib import Path
import base64
from io import BytesIO

from PIL import Image, ImageDraw


class ImageExtractor:
    def __init__(self, file: Path, out_filename, out=".", mode=1, padding=0):
        self.filename = file.stem
        self.padding = padding
        self.out = out
        self.out_filename = out_filename
        self.mode = mode
        self.tree = utils.parse_file(str(file))
        self.xml = PAGEBuilder(tree=self.tree, filename=self.out_filename)

    def export_image(self):
        with open(Path(self.out, self.out_filename).with_suffix(".png"), "wb") as image_file:
            image = base64.decodebytes(self.xml.image["base64"])

            if self.mode == 1:
                image_file.write(image)
            if self.mode == 2:
                self.export_lines(image)
            elif self.mode == 3:
                image = self.draw_lines(image)
                image_file.write(image)

    def export_lines(self, image):
        image = Image.open(BytesIO(image)).convert("RGB")
        lines_coords = self.xml.get_line_coords()

        for line_name, line_coords in enumerate(lines_coords):
            if not line_coords:
                continue

            if self.padding:
                line_coords = list([coord+self.padding for coord in line_coords])

            line_image = image.crop(line_coords)

            with open(Path(self.out, "_".join([self.out_filename,
                                               str(line_name).zfill(3)])).with_suffix(".png"), "wb") as line_out:
                line_image.save(line_out)

    def draw_lines(self, image):
        image = Image.open(BytesIO(image)).convert("RGB")
        draw = ImageDraw.Draw(image)
        lines = self.xml.get_line_coords()

        for line in lines:
            draw.rectangle(xy=line, outline="green")

        img_bytes = BytesIO()
        image.save(img_bytes, format="png")

        return img_bytes.getvalue()

