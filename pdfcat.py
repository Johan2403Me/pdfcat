import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", help="name of final merged PDF file")
    parser.add_argument("input_files", help="list of PDF files to merge", nargs='+')
    args = parser.parse_args()
    
    return args.output_file, args.input_files

def main():
    output_file, input_files = parse_args()

    print(f"Output file: {output_file}")
    print(f"Input files: {input_files}")


if __name__ == "__main__":
    main()
