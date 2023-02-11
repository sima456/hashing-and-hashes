import argparse
import ppdeep

def generate_fuzzy_hash(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        fuzzy_hash = ppdeep.hash(content)
        print(f"Fuzzy Hash for {filename}: {fuzzy_hash}")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate fuzzy hash for a file using ppdeep')
    parser.add_argument('filename', type=str, help='File to generate fuzzy hash for')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    generate_fuzzy_hash(args.filename)

if __name__ == '__main__':
    main()
