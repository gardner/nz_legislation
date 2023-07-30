
import chardet
import glob
import json
import argparse
import re

parser = argparse.ArgumentParser(description='Convert files to UTF-8')
parser.add_argument('-p', '--path', type=str, required=False, default='act/**/*.xml',
                    help='path to the files. accepts a glob pattern (e.g. act/**/*.xml)')
args = parser.parse_args()
files = glob.glob(args.path, recursive=True)

def convert(file, in_enc="ascii", out_enc="utf-8"):
    try:
        # print("convert " + file + " from " + in_enc + " to " + out_enc)
        content = open(file, 'rb').read()
        new_content = content.decode(in_enc).encode(out_enc)
        open(file, 'wb').write(new_content)
    except:
        print("error when convert " + file)

for file in files:
    with open(file, 'rb') as f:
        result = chardet.detect(f.read())  # or readline if the file is large
        encoding = result.get('encoding', 'utf-8')
        if encoding != 'utf-8':
            print(file + " - " + json.dumps(result))
            convert(file, encoding, 'utf-8')
        # print()
        # print(json.dumps(result) + " - " + file)
