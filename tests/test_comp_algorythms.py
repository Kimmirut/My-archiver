import pytest
import sys


sys.path.append('C:\\Users\\зелим\\Desktop\\programing\\folders\\projects\\my_archiver')


from src.comp_alorythms import *


class TestRLE:

    # 1. Tests for rle_encode.


    # 1.1 Validation tests.

    def test_type_error_raised(self):
        '''Tests if non-string types throws exception (They should).'''

        types = [
            1, 1.5, True, False, None, complex(12, 5),
            ('a', 1), [1, 2], {1: 'a', 2: 'b'},
            {1, 2, 3, 3}, frozenset([1, 2, 3]),
            ]

        for obj in types:
            with pytest.raises(TypeError):
                rle_encode(obj)

    def test_type_error_not_raised(self):
        '''
        Tests if encode method raises exception if str is given
        (it shouldn't)
        '''

        rle_encode('1234')
        rle_encode(';lsakjf;alkfjl;kajf;lkasdjflkag foipahaohf9p34h p8f-4 q3f9uq4-9ifu vp-poh vf h v9qi ohhgihjno viqpjvhn fniqj9 8b9ptnihf98piuhqiofhvaoihjpsfdohglksfkgjfkghhfhghghghgjkfghv5tohuqg [ior  ioqpopq ]')
        rle_encode('qqqqqqqwwwwejalk;jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')

    def test_value_error_raised(self):
        '''rle_encode should raise ValueError if given a string with length < 4'''

        with pytest.raises(ValueError):
            rle_encode('')
            rle_encode('1')
            rle_encode('12')
            rle_encode('123')

        rle_encode('1234')  # Shouldn't raise an error


    # 1.2 Tests on repetitive sequences.

    def test_repetitive_sequence(self):
        '''
        Excpectable behaviour is that function returns encoded string
        that must look like:
        'char_count1(char1)char_count2(char2)...char_countn(charn)'
        '''

        assert rle_encode('aaaa') == '4(a)'
        assert rle_encode('1111aaaKK') == '4(1)3(a)2(K)'

    def test_long_repetitive_sequence(self):
        '''
        Same as previous, but sequences get longer.
        '''
        assert rle_encode('a' * 164) == '164(a)'
        assert rle_encode('a' * 164 + 'q' * 66) == '164(a)66(q)'

    def test_non_repetitive_sequence(self):
        assert rle_encode('1234') == '-4(1234)'
        assert rle_encode('11234456') == '2(1)-2(23)2(4)-2(56)'

    def test_generic_rle_encode(self):
        assert rle_encode('AAAA') == '4(A)'
        assert rle_encode('111AAA') == '3(1)3(A)'
        assert rle_encode('KKYPYT') == '2(K)-4(YPYT)'
        assert rle_encode('KKYPYTT') == '2(K)-3(YPY)2(T)'



