import os
import sys
import argparse

from .fdown import FDown
from huepy import *


def client():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="File URL")
    parser.add_argument("-n", "--name", help="set file name")
    parser.add_argument("-p", "--path", help="set file path")
    parser.add_argument("-r", "--resume", action="store_true", help="resume getting a partially-downloaded file")
    parser.add_argument("-y", "--yes", action="store_false", help="download file without confirm download")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    if not args.url:
        print(info(red("Please Enter URL!")))
        sys.exit()

    if not args.name: args.name = args.url.split("/")[-1]
    if not args.path: args.path = ""

    fdown = FDown()

    if not os.path.isfile(args.path + args.name):
        fdown.download(args.url, args.name, args.path, args.yes)

    elif os.path.isfile(args.path + args.name) and (args.resume == True):
        fdown.download(args.url, args.name, args.path, args.yes)

    else:
        print(info(orange("Error: This file already exists. Please use '-r' parameter.")))


if __name__ == "__main__":
    client()

