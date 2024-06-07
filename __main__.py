import sys
import os
import glob
from src.comp_alorythms import *


if len(sys.argv) != 3:
    exit(print('Введите название файла и название методаа чтобы применить'))

_, file_name, method = sys.argv

if file_name not in glob.glob1('.', file_name):
    exit(print('Введите имя файла находящееся в текущей папке'))

if method not in ('compress, decompress'):
    exit(print('Введите корректное имя метода'))

if method == 'compress':

    with open(file_name) as file:

        file = file.read()
        methods = []

        if method == 'compress':
            if len(file) > 1000:
                compressed = str(lz77_encode(file))
                methods.append('lz77_encode')
            else:
                compressed = file

            compressed, codes = Huffman_encode(compressed)
            methods.append('Huffman_decode')

            print('compressed:\n' + str(compressed))
            # Creating folder with compressed files.

            compressed_dir_name = file_name + '.compressed'
            os.makedirs(compressed_dir_name)

            with open(f'{compressed_dir_name}/methods.txt', 'w') as methods_file,\
                open(f'{compressed_dir_name}/compressed.bin', 'wb') as compressed_file:

                compressed_file.write(bytes(compressed, 'utf-8'))

                methods_file.writelines(methods)

if method == 'decompress':
    archive = file_name
    with open(f'{archive}.compressed/compressed.bin') as compressed_file,\
         open(f'{archive}.compressed/methods.txt') as methods_file:

        compressed_data = compressed_file.read()
        methods = methods_file.read().split('\n')[:-1]

        for method in methods:
            compressed_data = eval(method)(compressed_data)

        print(compressed_data)




# & C:/Users/зелим/AppData/Local/Programs/Python/Python312/python.exe c:/Users/зелим/Desktop/My-archiver test1 decompress
