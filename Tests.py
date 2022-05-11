import unittest
import os

from bitarray import bitarray

from ByteHelper import ByteHelper
from HuffmanFileZipper import HuffmanFileZipper
from HuffmanLogic import HuffmanLogic


class TestHuffman(unittest.TestCase):

    def tearDown(self) -> None:
        for path in ['./rtest.txt', './test.txt', './test.txthuff', './test.txtkey']:
            if os.path.exists(path):
                os.remove(path)

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
        d = {0: 0.25, 1: 0.25, 2: 0.5}
        tree = ByteHelper.get_tree_from_freq_table(d)
        expected = (2, (0, 1))
        self.assertEqual(expected, tree)

    def test_encode(self):
        freq_t = ByteHelper.get_frequency_table(b"0111")
        dec_tree = ByteHelper.get_tree_from_freq_table(freq_t)
        en_t = {}
        HuffmanLogic.get_encode_table(dec_tree, en_t, bitarray())
        enc = HuffmanLogic.encode(en_t, b"0111")
        self.assertEqual(enc, bitarray('000001000000000000000000000000000111'))

    def test_decode(self):
        freq_t = ByteHelper.get_frequency_table(b"0111")
        dec_tree = ByteHelper.get_tree_from_freq_table(freq_t)
        en_t = {}
        HuffmanLogic.get_encode_table(dec_tree, en_t, bitarray())
        enc = HuffmanLogic.encode(en_t, b"0111")
        res = HuffmanLogic.decode(dec_tree, enc.tobytes())
        self.assertEqual(res, b"0111")
