import argparse
import pathlib
import glob

def validate_args(output_file, input_files):
    if pathlib.Path(output_file).suffix != ".pdf":
        print("error: output file name must end in .pdf")
        exit(1)
    elif len(input_files) < 2:
        print("error: need at least two valid files to merge")
        exit(1)

    for file in input_files:
        if pathlib.Path(file).suffix != ".pdf":
            print("error: input files must be a pdf")
            exit(1)


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

    print(f"Output file: {output_file}")
    print(f"Input files: {input_files}")


if __name__ == "__main__":
    main()
