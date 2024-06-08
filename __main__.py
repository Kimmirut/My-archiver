import json
import sys
import os
import glob
from src.comp_alorythms import *


# Command pallet arguments reading.

# To use:
# archiver <file_name> <method>

# Where:
# file_name - name of file that you want to compress/decompress.
# method - action that should be aplied to chosen file, can be:
#     - compress
#     - decompress

if len(sys.argv) != 3:
    exit(print('Введите название файла и название методаа чтобы применить'))

_, file_name, method = sys.argv

if file_name not in glob.glob1('.', file_name):
    exit(print('Введите имя файла находящееся в текущей папке'))

if method not in ('compress, decompress'):
    exit(print('Введите корректное имя метода'))


# Compressing file

if method == 'compress':

    with open(file_name) as file:

        file = file.read()
        methods = []  # list of methods needed to decompress file, filling during compression.

        if method == 'compress':
            if len(file) > 1000:
                compressed = str(lz77_encode(file))
                methods.append('lz77_encode')
            else:
                compressed = file

            compressed, codes = Huffman_encode(compressed)


            # Creating folder with compressed files.

            compressed_dir_name = file_name + '.compressed'
            os.makedirs(compressed_dir_name)

            with open(f'{compressed_dir_name}/methods.txt', 'w') as methods_file,\
                 open(f'{compressed_dir_name}/compressed.bin', 'wb') as compressed_file,\
                 open(f'{compressed_dir_name}/Huffman_codes.json', 'w') as codes_file:

                compressed_file.write(bytes(compressed, 'utf-8'))

                methods_file.writelines(methods)

                json.dump(codes, codes_file)

if method == 'decompress':

    archive = file_name
    with open(f'{archive}/compressed.bin') as compressed_file,\
         open(f'{archive}/methods.txt') as methods_file,\
         open(f'{archive}/Huffman_codes.json') as codes_file:

        compressed_data = compressed_file.read()

        codes = json.load(codes_file)
        compressed_data = Huffman_decode(compressed_data, codes)

        methods = methods_file.read().split('\n')[:-1]

        for method in methods:
            compressed_data = eval(method)(compressed_data)

    with open(file_name.removesuffix('.compressed'), 'w') as decompressed_file:
        decompressed_file.write(compressed_data)




# & C:/Users/зелим/AppData/Local/Programs/Python/Python312/python.exe c:/Users/зелим/Desktop/My-archiver test1.compressed decompress
