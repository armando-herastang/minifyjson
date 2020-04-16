import argparse
import json

REMOVABLE_CHARS = {
    '\n' : "New line",
    ' ': "Whitespace"
}

DOUBLE_QUOTE = "\""
class JSONMinifier():
    def __init__(self, filepath):
        self.input_path = filepath

    def minify_sequential(self):
        try:
            with open(self.input_path, 'r') as iFile, open("output.json", 'w') as oFile:
                insideQuotes = False
                while(True):
                    c = iFile.read(1)
                    if not c:
                        break
                    insideQuotes = c == DOUBLE_QUOTE
                    if not insideQuotes:
                        if c not in REMOVABLE_CHARS:
                            oFile.write(c)
                    else:
                        oFile.write(c)
        except FileNotFoundError as noFileError:
            print(noFileError)



if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Minify JSON file")
    arg_parser.add_argument(type=str, help="Path to the JSON file", dest="filepath")
    args = arg_parser.parse_args()

    minifier = JSONMinifier(args.filepath)
    minifier.minify_sequential()
