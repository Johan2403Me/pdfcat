import argparse
import pathlib
import glob
import sys

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
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", help="name of final merged PDF file")
    parser.add_argument("input_files", help="list of PDF files to merge", nargs='+')
    args = parser.parse_args()

    input_files = [file for arg in args.input_files for file in glob.glob(arg)]
    input_files.sort()

    validate_args(args.output_file, input_files)
    
    return args.output_file, input_files

def main():
    output_file, input_files = parse_args()
    merge_pdfs(output_file, input_files)

if __name__ == "__main__":
    main()
