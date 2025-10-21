import argparse
import glob

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", help="name of final merged PDF file")
    parser.add_argument("input_files", help="list of PDF files to merge", nargs='+')
    args = parser.parse_args()

    input_files = [file for arg in args.input_files for file in glob.glob(arg)]
    input_files.sort()
    
    return args.output_file, input_files

def main():
    output_file, input_files = parse_args()

    print(f"Output file: {output_file}")
    print(f"Input files: {input_files}")


if __name__ == "__main__":
    main()
