"""Command-line (script) interface to instapy"""

import argparse
from secrets import choice
import sys

import numpy as np
from PIL import Image

import instapy
from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file)
    if scale != 1:
        # Resize image, if needed
        image = image.resize((image.width // scale, image.height // scale))

    # Apply the filter
    func = instapy.get_filter(filter, implementation)
    filtered = func(np.asarray(image))
    if out_file:
        io.write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser("This is a test")

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    parser.add_argument("-g", "--gray", action='store_true', help="Select gray filter")
    parser.add_argument("-s", "--sepia", action='store_true', help="The output filename")
    parser.add_argument("-sc", "--scale", default=1, help="Scale factor to resize image")
    parser.add_argument("-i", "--implementation", choices=["python","numba","numpy"], default="numpy", help="The implementation")

    # parse arguments and call run_filter
    args = parser.parse_args()

    filter = "color2gray"
    if args.gray:
        filter = "color2gray"
    elif args.sepia:
        filter = "color2sepia"

    run_filter(args.file, args.out, args.implementation, filter, int(args.scale))