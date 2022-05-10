from HuffmanFileZipper import HuffmanFileZipper
import argparse

parser = argparse.ArgumentParser(description="Huffman zipper and unzipper")
parser.add_argument('type', type=str, help="e to encode, d to decode")
parser.add_argument('inpath', type=str, help="path to input file")
parser.add_argument('key', type=str, help="path to key creation/validation")
parser.add_argument('outpath', type=str, help="path to output")
args = parser.parse_args()

if args.type == "e":
    try:
        HuffmanFileZipper.zip_file(args.inpath, args.key, args.outpath)
        print("zipped!")
    except Exception as e:
        print("something is went wrong.")
        print(e)
elif args.type == "d":
    try:
        HuffmanFileZipper.unzip_file(args.inpath, args.key, args.outpath)
        print("unzipped!")
    except Exception as e:
        print("something is went wrong.")
        print(e)
else:
    print("в типе либо e пиши либо d пиши хорошее пиши плохое не пиши")