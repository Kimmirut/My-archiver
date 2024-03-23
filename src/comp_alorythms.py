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
            if cnt_non_rep != 1:
                encoded += get_non_rep_seq(end_of_seq_ind=i, length=cnt_non_rep + 1,
                                           string=data)
                cnt_non_rep = 1
        else:
            if cnt_rep != 1:
                encoded += get_rep_seq(curr, length=cnt_rep)
                cnt_rep = 1
                continue

            next_next = data[i+2] if i+2 < len(data) else None
            if next_next == next:
                encoded += get_non_rep_seq(end_of_seq_ind=i, length=cnt_non_rep,
                                           string=data)
                cnt_non_rep = 1
                continue

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


def rle_decode():
    raise NotImplementedError


__all__: list[str] = ['rle_encode', 'rle_decode']


if __name__ == '__main__':
    data = 'ККУРУТТ'
    res = rle_encode(data)
    print(res)
