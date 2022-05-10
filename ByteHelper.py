class ByteHelper:
    """Облегчает работу с байтами, текстом"""

    @staticmethod
    def get_frequency_table(text):
        """Получить таблицу частоты встречаемости символов"""
        table = {}
        const = 1 / len(text)
        for i in range(256):
            table[i] = 0
        for i in range(len(text)):
            current_byte = text[i:i + 1]
            current_int = int.from_bytes(current_byte, "little")
            table[current_int] += const

        return table

    @staticmethod
    def get_tree_from_freq_table(freq_table):
        """Возвращает отсортированное дерево частоты встречаемости символов. Структура дерева задана скобочной
        последовательностью))"""
        freq_table = dict(sorted(freq_table.items(), key=lambda item: item[1]))
        while len(freq_table) > 1:
            iterator = iter(freq_table.items())
            first = next(iterator)
            second = next(iterator)
            freq_table.pop(first[0])
            freq_table.pop(second[0])
            if first[1] + second[1] != 0:
                freq_table[(first[0], second[0])] = first[1] + second[1]
                freq_table = dict(sorted(freq_table.items(), key=lambda item: item[1]))

        return list(freq_table.keys())[0]
