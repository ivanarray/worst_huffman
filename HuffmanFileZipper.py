import pickle

from bitarray import bitarray

from HuffmanLogic import HuffmanLogic


class HuffmanFileZipper:
    @staticmethod
    def zip_file(filename, key_path, output_path):
        with open(filename, "rb") as f:
            content = f.read()

        from ByteHelper import ByteHelper
        freq_table = ByteHelper.get_frequency_table(content)
        decode_table = ByteHelper.get_tree_from_freq_table(freq_table)
        encode_table = {}
        HuffmanLogic.get_encode_table(decode_table, encode_table, bitarray())
        encoded = HuffmanLogic.encode(encode_table, content)
        encoded_bytes = encoded.tobytes()

        with open(key_path, "wb") as codetable:
            codetable.write(pickle.dumps(decode_table))

        with open(output_path, "wb") as encoded_f:
            encoded_f.write(encoded_bytes)

    @staticmethod
    def unzip_file(filename, key_path, output_path):
        with open(key_path, "rb") as dt:
            decode_table = pickle.loads(dt.read())

        with open(filename, "rb") as in_f:
            content = in_f.read()

        dc = HuffmanLogic.decode(decode_table, content)

        with open(output_path, "wb") as of:
            of.write(dc)
