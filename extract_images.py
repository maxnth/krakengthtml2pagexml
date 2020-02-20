from src.Extractor.extractor import ImageExtractor

import argparse
import enum
from pathlib import Path


class Mode(enum.IntEnum):
    PLAIN = 1
    LINES = 2
    LINESDRAWN = 3

    def __str__(self):
        return self.name.lower()

    def __repr__(self):
        return str(self)

    @staticmethod
    def argparse(s):
        try:
            return Mode[s.upper()]
        except KeyError:
            return s


def main():
    parser = argparse.ArgumentParser(description="Extracts various image versions (lines, …) from Kraken HTML GT")

    parser.add_argument("-i", "--input", help="Input file or directory.", required=True)
    parser.add_argument("-o", "--output", default=".", help="Output dir. Default saves to directory where script is "
                                                            "called.")
    parser.add_argument("-m", "--mode", help="Choose image export mode.", type=Mode.argparse, choices=list(Mode),
                        default="PLAIN")
    parser.add_argument("-p", "--padding", help="Padding for line extraction (in pixel)", type=int,
                        default=0)
    parser.add_argument("-e", "--enumerate", dest='enumerate', action='store_true',
                        help="Enumerate output filename instead of using input filename.")
    parser.add_argument("-es", "--enumerate-start", default=1, help="If enumerate flag is set, determines starting"
                                                                    " number")

    args = vars(parser.parse_args())

    return args


if __name__ == "__main__":
    args = main()

    print("Converting files...")

    in_path = args["input"]
    out_path = args["output"]

    for num, file in enumerate(sorted(Path(in_path).glob("*.html")), start=int(args["enumerate_start"])):
        print("Converting {filename}...".format(filename=file.stem))

        if args.get("enumerate"):
            out_name = str(num).zfill(4)
        else:
            out_name = file.stem

        if args["mode"] == 2:
            Path(out_path, out_name).mkdir(exist_ok=True)
            _out_path = Path(out_path, out_name)
        else:
            _out_path = out_path

        conv = ImageExtractor(file=file, out=_out_path, out_filename=out_name, mode=args["mode"], padding=args["padding"])
        conv.export_image()

    print("Conversion successful.")
