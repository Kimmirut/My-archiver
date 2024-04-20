import pytest
import sys


sys.path.append('C:\\Users\\зелим\\Desktop\\programing\\folders\\projects\\my_archiver')


from src.comp_alorythms import *
from src.comp_alorythms import get_frequency_table


class TestRLEEncode:

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


class TestRLEDecode:

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
                rle_decode(obj)

    def test_type_error_not_raised(self):
        '''
        Tests if encode method raises exception if str is given
        (it shouldn't)
        '''

        rle_decode('1234')
        rle_decode(';lsakjf;alkfjl;kajf;lkasdjflkag foipahaohf9p34h p8f-4 q3f9uq4-9ifu vp-poh vf h v9qi ohhgihjno viqpjvhn fniqj9 8b9ptnihf98piuhqiofhvaoihjpsfdohglksfkgjfkghhfhghghghgjkfghv5tohuqg [ior  ioqpopq ]')
        rle_decode('qqqqqqqwwwwejalk;jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')

    def test_value_error_raised(self):
        '''rle_decode should raise ValueError if given a string with length < 4'''

        with pytest.raises(ValueError):
            rle_decode('')
            rle_decode('1')
            rle_decode('12')
            rle_decode('123')

        rle_decode('1234')  # Shouldn't raise an error


    # 1.2 Tests on repetitive sequences.

    def test_repetitive_sequence(self):
        '''
        Excpectable behaviour is that function returns encoded string
        that must look like:
        'char_count1(char1)char_count2(char2)...char_countn(charn)'
        '''

        assert rle_decode('4(a)') == 'aaaa'
        assert '1111aaaKK' == rle_decode('4(1)3(a)2(K)')

    def test_long_repetitive_sequence(self):
        '''
        Same as previous, but sequences get longer.
        '''
        assert 'a' * 164 == rle_decode('164(a)')
        assert 'a' * 164 + 'q' * 66 == rle_decode('164(a)66(q)')

    def test_non_repetitive_sequence(self):
        assert '1234' == rle_decode('-4(1234)')
        assert '11234456' == rle_decode('2(1)-2(23)2(4)-2(56)')

    def test_generic_rle_decode(self):
        assert 'AAAA' == rle_decode('4(A)')
        assert '111AAA' == rle_decode('3(1)3(A)')
        assert 'KKYPYT' == rle_decode('2(K)-4(YPYT)')
        assert 'KKYPYTT' == rle_decode('2(K)-3(YPY)2(T)')


class TestHuffmanEncode:

    def test_get_frequency_table(self):
        assert get_frequency_table('') == {}
        assert get_frequency_table('a') == {'a':1}
        assert get_frequency_table('aaaabcbbd') == {'a': 4, 'b': 3, 'c': 1, 'd': 1}

    @pytest.fixture
    def Node(self):
        return namedtuple('Node', ('data', 'left', 'right'))

    @pytest.fixture
    def Leaf(self):
        return namedtuple('Leaf', ('data',))

    @pytest.fixture
    def tree(self):
        '''
        codes tree as "Node" object for "aaaabbcd" string
        with the following structure:

                (abcd:8)
                /      \
            (a:4)      (bcd:4)
                       /     \
                   (b:2)     (cd:2)
                             /    \
                         (c:1)    (d:1)
        '''

        return Node(data=(8, 'abcd'), left=Leaf(data=(4, 'a')), right=Node(data=(4, 'bcd'), left=Leaf(data=(2, 'b')), right=Node(data=(2, 'cd'), left=Leaf(data=(1, 'c')), right=Leaf(data=(1, 'd')))))

    def test_build_code_tree_1(self, tree):
        freq_table: dict[str, int] = {'a': 4, 'b': 2, 'c': 1, 'd': 1}

        assert build_code_tree(freq_table) == tree

    # Edge cases.
    def test_build_code_tree_one_symbol(self, Leaf):
        freq_table: dict[str, int] = {'a': 3}

        tree = Leaf(data=(3, 'a'))

        assert build_code_tree(freq_table) == tree

    def test_build_code_tree_one_symbol_2(self, Leaf):
        freq_table: dict[str, int] = {'a': 1}

        tree = Leaf(data=(1, 'a'))

        assert build_code_tree(freq_table) == tree

    def test_get_code(self, tree):
        codes: dict = {
            'a': '0', 'b': '10',
            'c': '110', 'd': '111'
        }

        for char in codes:
            assert get_code(tree, char) == codes[char]

    def test_get_code_edge_case(self):
        tree = Leaf(data=(1, 'a'))
        assert get_code(tree, 'a') == '0'

    def test_get_codes_from_tree(self, tree):
        chars: tuple = ('a', 'b', 'c', 'd')
        codes: dict = {'b': '10', 'a': '0', 'd': '111', 'c': '110'}

        assert get_codes_from_tree(chars, tree) == codes

    def test_get_codes_from_tree(self):
        chars: tuple = ('a',)
        tree = Leaf((1, 'a'))
        codes: dict = {'a': '0'}

        assert get_codes_from_tree(tree, chars) == codes

    def test_Huffman_encode(self):
        data: str = 'aaaabbcd'
        encoded, codes = Huffman_encode(data)

        assert codes == {'0': 'a', '10': 'b', '110': 'c', '111': 'd'}
        assert encoded == '00001010110111'

    def test_Huffman_encode_edge_case_1(self):
        data: str = 'aaaa'
        encoded, codes = Huffman_encode(data)

        assert codes == {'0': 'a'}
        assert encoded == '0000'

    def test_Huffman_encode_edge_case_2(self):
        data: str = 'a'
        encoded, codes = Huffman_encode(data)

        assert codes == {'0': 'a'}
        assert encoded == '0'


class TestHuffmanDecode:

    def test_invert_dict(self):
        d = {}
        invert_dict(d)
        assert d == {}

        d = {'a': 1}
        invert_dict(d)
        assert d == {1: 'a'}

        d = {'a': '1', 'b': '2', 'c': '3'}
        invert_dict(d)
        assert d == {'1': 'a', '2': 'b', '3': 'c'}

    def test_Huffman_decode_edge_case1(self):
        assert Huffman_decode('', {}) == ''

    def test_Huffman_decode_edge_case2(self):
        assert Huffman_decode('0', {'0': 'a'}) == 'a'

    def test_Huffman_decode_edge_case3(self):
        assert Huffman_decode('0000', {'0': 'a'}) == 'aaaa'

    def test_Huffman_decode1(self):
        encoded = '00001010110111'
        codes = {'0': 'a', '10': 'b', '110': 'c', '111': 'd'}

        decoded = Huffman_decode(encoded, codes)

        assert decoded == 'aaaabbcd'

    def test_Huffman_decode2(self):
        encoded = '100010011001101101101000000000101010101111111111111'
        codes = {'1000': '1', '1001': '2', '101': '3', '00': '4', '01': '5', '11': '6'}

        decoded = Huffman_decode(encoded, codes)

        assert decoded == '122333444455555666666'

class TestAriphmeticEncode:
    # TODO: Add fixtures.

    def test_get_frequency_table_float(self):
        data = 'abac'
        freq_table_float = {
            'a': 0.50,
            'b': 0.25,
            'c': 0.25,
        }

        assert get_frequency_table_float(data) == freq_table_float

    def test_get_frequency_table_float_edge_case1(self):
        data = 'a'
        freq_table_float = {
            'a': 0.100,
        }

        assert get_frequency_table_float(data) == freq_table_float

    def test_get_frequency_table_float_edge_case1(self):
        data = ''
        freq_table_float = {}

        assert get_frequency_table_float(data) == freq_table_float

    def test_get_subsegments(self):
        freq_table = {
            'a': 0.50,
            'b': 0.25,
            'c': 0.25,
        }

        segment = Segment(0.0, 1.0, '')

        subsegments = [
            Segment(0.0, 0.5, 'a'),
            Segment(0.5, 0.75, 'b'),
            Segment(0.75, 1.0, 'c'),
        ]

        assert get_subsegments(segment, freq_table) == subsegments

    def test_get_subsegments_edge_case_2(self):
        freq_table = {}

        segment = Segment(0.0, 1.0, '')

        subsegments = []

        assert get_subsegments(segment, freq_table) == subsegments

    def test_get_subsegments_edge_case_2(self):
        freq_table = {
            'a': 1.0,
        }

        segment = Segment(0.0, 1.0, '')

        subsegments = [
            Segment(0.0, 1.0, 'a'),
        ]

        assert get_subsegments(segment, freq_table) == subsegments

    def test_get_subsegments_full(self):
        # full cycle for data = abac.

        freq_table = {
            'a': 0.50,
            'b': 0.25,
            'c': 0.25,
        }

        # First divide.

        working_segment = Segment(0.0, 1.0, '')
        subsegments = [
            Segment(start=0.0, end=0.5, char='a'),
            Segment(start=0.5, end=0.75, char='b'),
            Segment(start=0.75, end=1.0, char='c'),
        ]

        assert get_subsegments(working_segment, freq_table) == subsegments

        #choosing "a"

        # Second divide. Segment with "a" chosen as working.

        working_segment = Segment(start=0.0, end=0.5, char='a')
        subsegments = [
            Segment(start=0.0, end=0.25, char='a'),
            Segment(start=0.25, end=0.375, char='b'),
            Segment(start=0.375, end=0.5, char='c'),
        ]

        #choosing "b"

        assert get_subsegments(working_segment, freq_table) == subsegments

        # Third divide. Segment with "b" chosen as working.

        working_segment = Segment(start=0.25, end=0.375, char='b')
        subsegments = [
            Segment(start=0.25, end=0.3125, char='a'),
            Segment(start=0.3125, end=0.34375, char='b'),
            Segment(start=0.34375, end=0.375, char='c'),
        ]

        assert get_subsegments(working_segment, freq_table) == subsegments
        # choosing "a"

        # Fourth divide. Segment with "a" chosen as working.

        working_segment = Segment(start=0.25, end=0.3125, char='a')
        subsegments = [
            Segment(start=0.25, end=0.28125, char='a'),
            Segment(start=0.28125, end=0.296875, char='b'),
            Segment(start=0.296875, end=0.3125, char='c'),
        ]

        assert get_subsegments(working_segment, freq_table) == subsegments

        #choosing "c"

        # Number from c is result of encoding.

    def test_ariphmetic_encode(self):
        data = 'abac'
        assert 0.296875 <= ariphmetic_encode(data) <= 0.3125

