from bitarray import bitarray

class HuffmanLogic:
    """Класс внутренней логики кодирования"""

    @staticmethod
    def encode(encode_table, content):
        """Возвращает массив битов по таблице кодирования и содержимому"""
        result = bitarray()
        result.frombytes(len(content).to_bytes(4, "little"))
        for i in range(len(content)):
            current_byte = content[i:i + 1]
            current_int = int.from_bytes(current_byte, "little")
            for j in encode_table[current_int]:
                result.append(j)

        return result

    @staticmethod
    def decode(decode_table, encoded):
        """возвращает содержимое по таблице декодинга и закодированному содержимому"""
        length = int.from_bytes(encoded[0:4], "little")
        temp_table = decode_table
        result = bytearray()
        ba = bitarray()
        ba.frombytes(encoded)
        counter = 32
        end_counter = 0
        for e in ba:
            if counter > 0:
                counter -= 1
                continue

            if end_counter == length:
                return result
            temp_table = temp_table[e]
            if type(temp_table) is int:
                end_counter += 1
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
