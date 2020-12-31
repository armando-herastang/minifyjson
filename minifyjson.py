import argparse

class JSONMinifier():
    def __init__(self, filepath):
        self.input_path = filepath
        self.output_path = "output.json"

    def minify_sequential(self):
        try:
            with open(self.input_path, 'r') as iFile, open(self.output_path, 'w') as oFile:
                insideDoubleQuotes = False
                while(True):
                    c = iFile.read(1)
                    if not c:
                        break
                    if c == DOUBLE_QUOTE:
                        insideDoubleQuotes = not insideDoubleQuotes
                    if not insideDoubleQuotes:
                        if c not in REMOVABLE_CHARS:
                            oFile.write(c)
                    else:
                        oFile.write(c)
            print(f"JSON minified to: {self.output_path}")
        except FileNotFoundError as noFileError:
            print(noFileError)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Minify JSON file")
    arg_parser.add_argument(type=str, help="Path to the JSON file", dest="filepath")
    args = arg_parser.parse_args()

    minifier = JSONMinifier(args.filepath)
    minifier.minify_sequential()
