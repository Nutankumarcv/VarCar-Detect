import argparse

from mains import main
import numpy as np

parser = argparse.ArgumentParser(
    formatter_class= argparse.ArgumentDefaultsHelpFormatter,
    description=
    """
    Speed estimation application to get started - varcar.exe --help or varcar.exe -h for help
    """
)

parser.add_argument("--source", default=0, type=int, help='source of input (webcam or video )')
parser.add_argument("--output", help='output folder', default='../output.mp4')

args = parser.parse_args()


main(source= args.source, output= args.output)
