from HuffmanFileZipper import HuffmanFileZipper

name = "test.txt"
HuffmanFileZipper.zip_file(name, name + "key", name + "huff")
print("zipped!")
HuffmanFileZipper.unzip_file(name + "huff", name + "key", "r" + name)
print("unzipped!")
