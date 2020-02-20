# krakengthtml2pagexml
quick and dirty conversion tool for a specific use case

```
usage: convert.py [-h] -i INPUT [-o OUTPUT] [-e] [-es ENUMERATE_START]

Converts one or more Kraken HTML Ground Truth files into basic PAGE XML.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file or directory.
  -o OUTPUT, --output OUTPUT
                        Output dir. Default saves to directory where script is called.
  -e, --enumerate       Enumerate output filename instead of using input filename.
  -es ENUMERATE_START, --enumerate-start ENUMERATE_START
                        If enumerate flag is set, determines starting number
```
```
usage: extract_images.py [-h] -i INPUT [-o OUTPUT] [-m {plain,lines,linesdrawn}] [-p PADDING] [-e] [-es ENUMERATE_START]

Extracts various image versions (lines, …) from Kraken HTML GT

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file or directory.
  -o OUTPUT, --output OUTPUT
                        Output dir. Default saves to directory where script is called.
  -m {plain,lines,linesdrawn}, --mode {plain,lines,linesdrawn}
                        Choose image export mode.
  -p PADDING, --padding PADDING
                        Padding for line extraction (in pixel)
  -e, --enumerate       Enumerate output filename instead of using input filename.
  -es ENUMERATE_START, --enumerate-start ENUMERATE_START
                        If enumerate flag is set, determines starting number
 ```
