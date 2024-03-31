'''
A module containing compressing algorythms, such as:

1. RLE - Run-Lenght Encoding.
(https://en.wikipedia.org/wiki/Run-length_encoding)

2. Huffman Encoding.
(https://en.wikipedia.org/wiki/Huffman_coding)

3. Huffman Encoding (Adaptive).
(https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)

4. Arithmetic coding.
(https://en.wikipedia.org/wiki/Arithmetic_coding)

5. Arithmetic coding (Adaptive)
(https://en.wikipedia.org/wiki/Context-adaptive_binary_arithmetic_coding)

6. LZ77, LZ78.
(https://neerc.ifmo.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B_LZ77_%D0%B8_LZ78)

'''


from collections import namedtuple
from dataclasses import dataclass
from typing import Any, Iterable, Self
import heapq as hpq


Node = namedtuple('Node', ('data', 'left', 'right'))
Leaf = namedtuple('Leaf', ('data',))


'''
"rle_encode" and "rle_decode" are functions to  compress data
according to RLE data compression alogrythm.
Suitable for data with sequences of long repetitive symbols.

Usage example:

rle_encode('aaaaa')
>>> 5(a)
rle_decode('5(a)')
>>> aaaaa

rle_encode('abcaaa')
>>> -3(abc)3(a)
rle_decode('-3(abc)3(a)')
>>> abcaaa
'''


def rle_encode(data: str) -> str:
    '''
    Ecoding given string according to RLE algoritm.
    Denotes repetitive sequence as "<repeats_number>(symbol)
    and non-repetitive as "<non-repeats>(symbols)."

    Raises TypeError if non-string is given,
    and ValueError if string is less than 4 in curracters.

    Usage example:

    rle_encode('aaaaa')
    >>> 5(a)
    rle_encode('abcaaa')
    >>> -3(abc)3(a)
    '''

    validate_string(data)

    # Counters to count lenghts of (none) repetitive sequences.
    cnt_rep: int = 1
    cnt_non_rep: int = 1
    encoded: str = ''

    for i in range(len(data) - 1):
        curr: str = data[i]
        next: str = data[i + 1]
        if next == curr:
            cnt_rep += 1
            if cnt_non_rep != 1:  # If non rep. sequence just ended.
                encoded += get_non_rep_seq(end_of_seq_ind=i, length=cnt_non_rep + 1,
                                           string=data)
                cnt_non_rep = 1   # Adding it into result
        else:
            if cnt_rep != 1:      # If rep. sequence just ended.
                encoded += get_rep_seq(curr, length=cnt_rep)
                cnt_rep = 1
                continue
            # Otherwise, it can be end of non-rep. sequence
            next_next: str = data[i+2] if i+2 < len(data) else None
            if next_next == next:
                encoded += get_non_rep_seq(end_of_seq_ind=i, length=cnt_non_rep,
                                           string=data)
                cnt_non_rep = 1
                continue
            # Or just another character in non-rep sequence
            cnt_non_rep += 1

    last_seq: str = ''
    if cnt_non_rep != 1:
        last_seq += get_non_rep_seq(end_of_seq_ind=i + 1, length=cnt_non_rep,
                                           string=data)
    else:
        last_seq += get_rep_seq(curr, length=cnt_rep)

    return encoded + last_seq


# Support functions for rle_encode.

def get_rep_seq(char: str, length: int) -> None:
    '''
    Formates repetitive sequence of "char" with "length" to and returns it.
    '''

    return f'{length}({char})'


def get_non_rep_seq(end_of_seq_ind: int, length: int, string: str) -> None:
    '''
    Returns non-repetitive sequence of string with given length and
    index to the end of non-rep sequence according to RLE algorithm.
    '''

    start_of_seq_ind: int = end_of_seq_ind - length + 1
    non_rep_seq: str = string[start_of_seq_ind:end_of_seq_ind + 1]

    return f'{-length}({non_rep_seq})'


def validate_string(data: str):
    '''
    Throws TypeError if "data" argument isn't a string and
    ValueError if it less than 4 characters in length.
    '''

    if not isinstance(data, str):
        raise TypeError('"data" argument should be type of str.')

    if len(data) < 4:
        raise ValueError('Encoding data chould have at least 4 characters')


def rle_decode(data: str) -> str:
    '''
    Decodes given RLE encoded string and returns it.

    Raises TypeError if non-string is given,
    and ValueError if string is less than 4 in curracters.

    Usage example:
    rle_decode('5(a)')
    >>> aaaaa
    rle_decode('-3(abc)3(a)')
    >>> abcaaa
    '''

    validate_string(data)

    decoded: str = ''
    count: str = '' # Contains lenght of (non) rep sequence.
    i: int = 0

    while i != len(data):
        if data[i] != '(':    # Writes number into count.
            count += data[i]
            i += 1
            continue

        # If curr char is "(", then it means a sequence.
        if count[0] == '-':    # Non-rep. sequence case.
            count = abs(int(count))
            seq: str = data[i + 1:i + count + 1]
            i = i + count + 2
            count = ''
        else:                  # Rep. sequence
            count = abs(int(count))
            seq: str = count * data[i + 1]
            i += 3
            count = ''

        decoded += seq

    return decoded


# Huffman code functions and everything related to it.

def Huffman_encode(data: str) -> tuple[dict[str], Node]:
    '''
    Encodes given string according to Huffman encoding algorithm,
    and returns tuple - (encoded: chars, codes: dict[char, code]).
    '''

    freq_table: dict[str, int] = get_frequency_table(data)
    codes_tree: object = build_code_tree(freq_table)
    codes: dict[str, int] = get_codes_from_tree(codes_tree, chars=freq_table.keys())

    encoded: str = ''
    for char in data:
        encoded += codes[char]

    return (encoded, codes)


def build_code_tree(freq_table: dict[str, int]) -> tuple:
    '''
    Builds a Huffman coding tree for given frequency table
    of characters, and returns tree as "Node" object.
    If "freq_table" has only one character - returns Leaf.
    '''

    heap: list = [Leaf(data=(freq_table[char], char)) for char in freq_table]
    hpq.heapify(heap)   # Building min heap to extract min nodes for O(1).

    while len(heap) > 1:           # Taking 2 nodes, and creating it's parent node.
        node1 = hpq.heappop(heap)  # Named tuple object can be compared by
        node2 = hpq.heappop(heap)  # their fields (field "data" contains frequency).
        freq1, char1 = node1.data  # They can be unpacked also.
        freq2, char2 = node2.data
        new_node: Node = Node(data=(freq1 + freq2, char1 + char2),
                              left=node1, right=node2,)
        hpq.heappush(heap, new_node)

    return hpq.heappop(heap)       # Last left node is final tree.


def get_codes_from_tree(tree: namedtuple, chars: Iterable) -> dict[str, str]:
    '''
    Takes tree of class 'Node' and Iterable object with chars which codes
    will be searched, and returnes them as dictionary: {char1: code1...}
    '''

    codes: dict[str, str] = {}
    for char in chars:
        codes[char] = get_code(tree, char)

    return codes


def get_code(tree: Node, char: str) -> str:
    '''
    Function that gets symbol code from given code tree, and returns it.
    '''

    if isinstance(tree, Leaf):  # If table contains only one character
        return '0'              # We assign 0 code to it

    curr: Node = tree
    code: str = ''

    while curr.data[1] != char:      # data[1] is string with characters
        if char in curr.left.data[1]:
            code += '0'
            curr = curr.left
        else:
            code += '1'
            curr = curr.right

    return code


def get_frequency_table(data: str|list) -> dict[str, int]:
    '''
    Taking an iteble object and returns a frequency table for it.
    '''

    freq_table: dict[str, int] = {}
    for char in data:
        freq_table[char] = freq_table.get(char, 0) + 1

    return freq_table
