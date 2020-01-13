import src.utils as utils
import src.PAGEXML.template as template

from datetime import datetime
import base64


class PAGEBuilder:
    def __init__(self, tree, filename, pretty=False):
        self.tree = tree
        self.filename = filename
        self.image = self.get_image()
        self.content = ""
        self.pretty = pretty

    def __str__(self):
        if self.pretty:
            return utils.prettify(self.content)
        else:
            return str(self.content)

    def get_image(self):
        img_type, img_base = utils.get_img_base64(self.tree)

        height, width = utils.get_img_size(base64.decodebytes(bytes(img_base, "utf-8")))
        return {"base64": bytes(img_base, "utf-8"), "format": img_type, "height": height, "width": width}

    def get_lines(self):
        return self.tree.xpath("//div[@class='column']/ul//li")

    def build_lines(self, region_id):
        lines = ""
        for line_num, line in enumerate(self.get_lines()):
            line_data = utils.create_line_dict(line)
            lines += template.TEXTLINE.format(_id="l{_lID}".format(_lID=str(line_num)),
                                              _points=utils.format_bbox(*line_data.get("line_bbox").split(", ")),
                                              _text=line_data.get("line_text"))
        return lines

    def build_text_region(self, region_id="r0", region_type="paragraph"):
        return template.TEXTREGION.format(_id=region_id, _type=region_type,
                                          _points=utils.format_bbox(*utils.calc_bbox(utils.get_all_cords(self.tree))),
                                          _text_lines=self.build_lines(region_id))

    def build_page(self):
        return template.PAGE.format(_content=self.build_text_region(), _img_height=self.image["height"],
                                    _img_width=self.image["width"], _img_name="{filename}.{ext}".format(
                filename=self.filename,
                ext=self.image["format"]))

    def build_skelethon(self):
        return template.SKELETHON.format(_metadata=template.METADATA.format(_time=datetime.now().isoformat()),
                                         _content=self.build_page())

    def build(self):
        self.content = self.build_skelethon()
