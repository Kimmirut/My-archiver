import sys
import glob
from src.comp_alorythms import *


if len(sys.argv) != 3:
    exit(print('Введите название файла и название методаа чтобы применить'))

_, file_name, method = sys.argv

if file_name not in glob.glob1('.', file_name):
    exit(print('Введите имя файла находящееся в текущей папке'))

if method not in ('compress, decompress'):
    exit(print('Введите корректное имя метода'))

with open(file_name) as file:

    file = file.read()
    if method == 'compress':
        compressed = lz77_encode(file)

        compressed, codes = Huffman_encode(compressed)

    print('compressed:\n' + str(compressed))
