import argparse

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Minify JSON file")
    arg_parser.add_argument(type=str, help="Path to the JSON file", dest="filepath")
    args = arg_parser.parse_args()