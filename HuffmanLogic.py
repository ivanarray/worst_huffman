from bitarray import bitarray


class HuffmanLogic:
    @staticmethod
    def encode(encode_table: dict[int, bitarray], content):
        result = bitarray()
        #result.frombytes(len(content).to_bytes(4, "little"))
        for i in range(len(content)):
            current_byte = content[i:i + 1]
            current_int = int.from_bytes(current_byte, "little")
            for j in encode_table[current_int]:
                result.append(j)

        return result

    @staticmethod
    def decode(decode_table, encoded):
        temp_table = decode_table
        result = bytearray()
        ba = bitarray()
        ba.frombytes(encoded)
        for e in ba:
            temp_table = temp_table[e]
            if type(temp_table) is int:
                result.append(temp_table)
                temp_table = decode_table
        return result

    @staticmethod
    def get_encode_table(decode_table, encode_table, symbol: bitarray):
        if type(decode_table) is tuple:
            left = bitarray(symbol)
            left.append(0)
            right = bitarray(symbol)
            right.append(1)
            HuffmanLogic.get_encode_table(decode_table[0], encode_table, left)
            HuffmanLogic.get_encode_table(decode_table[1], encode_table, right)
        else:
            encode_table[decode_table] = symbol
