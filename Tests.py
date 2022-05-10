import unittest

from bitarray import bitarray

from ByteHelper import ByteHelper
from HuffmanFileZipper import HuffmanFileZipper
from HuffmanLogic import HuffmanLogic


class TestHuffman(unittest.TestCase):

    def test_identical(self):
        filename = "test.txt"
        text = "A very nice text! I like it SO MUCH!"
        with open(filename, "w") as f:
            f.write(text)
        HuffmanFileZipper.zip_file(filename, filename + "key", filename + "huff")
        HuffmanFileZipper.unzip_file(filename + "huff", filename + "key", "r" + filename)
        with open("r" + filename, "r") as f:
            text2 = f.read()

        self.assertEqual(text2, text)

    def test_frequency_table(self):
        d = ByteHelper.get_frequency_table(b"0111")
        print(d)
        self.assertEqual(d[48], 0.25)
        self.assertEqual(d[49], 0.75)

    def test_get_tree(self):
        d = {}
        d[0] = 0.25
        d[1] = 0.25
        d[2] = 0.5
        tree = ByteHelper.get_tree_from_freq_table(d)
        expected = (2, (0, 1))
        self.assertEqual(expected, tree)

    def test_encode(self):
        d = ByteHelper.get_frequency_table(b"0111")
        t = ByteHelper.get_tree_from_freq_table(d)
        e = {}
        HuffmanLogic.get_encode_table(t, e, bitarray())
        ba = HuffmanLogic.encode(e, b"0111")
        self.assertEqual(ba, bitarray('000001000000000000000000000000000111'))
