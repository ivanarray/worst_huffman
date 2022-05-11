from HuffmanFileZipper import HuffmanFileZipper
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Huffman zipper and unzipper")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encode', action='store_true', help='compression mode')
    group.add_argument('-d', '--decode', action='store_true', help='decompression mode')
    parser.add_argument('inpath', type=str, help="path to input file")
    parser.add_argument('key', type=str, help="path to key creation/validation")
    parser.add_argument('outpath', type=str, help="path to output")
    args = parser.parse_args()

    if args.encode:
        try:
            HuffmanFileZipper.zip_file(args.inpath, args.key, args.outpath)
            print("zipped!")
        except Exception as e:
            print("something is went wrong.")
            print(e)
    elif args.decode:
        try:
            HuffmanFileZipper.unzip_file(args.inpath, args.key, args.outpath)
            print("unzipped!")
        except Exception as e:
            print("something is went wrong.")
            print(e)
    else:
        parser.print_help()
