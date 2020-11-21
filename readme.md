# minifyJSON

A simple script for minifying a `JSON` file.

## What is minification?

Minification refers to the process of removing unnecessary or redundant data without affecting how the resource is processed by the browser - e.g. code comments and formatting, removing unused code, using shorter variable and function names, and so on.

**Note:** Do not check if it is a valid `JSON` format. Assume it is correct and minify it.

## Usage

Just run:

```bash
python minifyjson.py path_to_file
```

It will create a `output.json` file on the current working directory. This file will contain the minify version of the input file.

## Todo

- [ ] Parse and argument to specify output path
- [ ] Figure out an easier way to do this
- [ ] Implement check of valid JSON file
- [ ] Implement beautify using identation
- [ ] Create a GUI using PyQT >= 5
