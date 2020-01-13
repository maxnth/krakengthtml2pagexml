from src.Converter.converter import Converter

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Converts one or more Kraken HTML Ground Truth files into basic PAGE XML.")

    parser.add_argument("-i", "--input", help="Input file or directory.", required=True)
    parser.add_argument("-o", "--output", default=".", help="Output dir. Default saves to directory where script is "
                                                            "called.")
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

        conv = Converter(file=file, out=out_path, out_filename=out_name)
        conv.export()

    print("Conversion successful.")
