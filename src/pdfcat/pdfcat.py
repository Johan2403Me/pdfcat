# Copyright (C) 2025 Johan Emmanuel

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import pathlib
import glob
import sys
from importlib.metadata import version

from natsort import natsorted
from pypdf import PdfWriter
from pypdf.errors import PdfStreamError

def merge_pdfs(output_file, input_files):
    merger = PdfWriter()

    for pdf in input_files:
        try:
            merger.append(pdf)
        except PdfStreamError:
            print(f"error: invalid or corrupted pdf file: {pdf}")
            merger.close()
            sys.exit(1)

    merger.write(output_file)
    merger.close()

def validate_args(output_file, input_files):
    if pathlib.Path(output_file).suffix != ".pdf":
        print("error: output file name must end in .pdf")
        sys.exit(1)
    elif len(input_files) < 2:
        print("error: need at least two valid files to merge")
        sys.exit(1)

    for file in input_files:
        if not pathlib.Path(file).is_file():
            print(f"error: {file}/ is a not a file")
            sys.exit(1)
        elif pathlib.Path(file).suffix != ".pdf":
            print(f"error: {file} is not a PDF")
            sys.exit(1)


def parse_args():
    prog = "pdfcat"
    parser = argparse.ArgumentParser(
        prog=prog,
        description="A simple tool to merge multiple PDFs at the command line."
    )
    parser.add_argument("output_file", help="name of final merged PDF file")
    parser.add_argument("input_files", 
                        help="list of PDF files to merge", nargs='+')
    parser.add_argument("-V", "--version", 
                        action="version", 
                        version=f"{prog} {version(prog)}")
    parser.add_argument("-s", "--sorted", 
                        action="store_true", 
                        help="merge the PDFs in an order sorted by name")

    args = parser.parse_args()

    input_files = [file for arg in args.input_files for file in glob.glob(arg)]
    
    if args.sorted:
        input_files = natsorted(input_files)

    validate_args(args.output_file, input_files)
    
    return args.output_file, input_files

def main():
    output_file, input_files = parse_args()
    merge_pdfs(output_file, input_files)
