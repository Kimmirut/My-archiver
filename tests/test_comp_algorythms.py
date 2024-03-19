import pytest
import sys


sys.path.append('C:\\Users\\зелим\\Desktop\\programing\\folders\\projects\\my_archiver')
print(sys.path)


from src.comp_alorythms import rle_encode


class TestRLE:

    class TestEncode:

        @pytest.mark.skip
        def test_validation(self):
            '''Tests type validation for RLE encode method'''

            raise NotImplementedError

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
            '''encode should raise ValueError if given a string with length < 4'''

            with pytest.raises(ValueError):
                rle_encode('')
                rle_encode('1')
                rle_encode('12')
                rle_encode('123')

            rle_encode('1234')  # Shouldn't raise an error

        def test_repetitive_sequence(self):
            '''

            '''

            assert rle_encode('aaaa') == '4(a)'
            assert rle_encode('1111aaaKK') == '4(1)3(a)2(KK)'

        @pytest.skip()
        def test_non_repetitive_sequence(self):
            '''

            '''

            assert rle_encode(1234) == '-4(1234)'



