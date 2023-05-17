#!/usr/bin/env python3
import json
import argparse

parser = argparse.ArgumentParser(description='Compares two configuration'
                                 ' files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()


def generate_diff(first_file, second_file):
    with open(first_file, 'r') as first_input:
        with open(second_file, 'r') as second_input:
            data1 = json.load(first_input)
            print(data1)
            data2 = json.load(second_input)
            print(data2)
    string = ''
    return string


'''
Ваша библиотека также должна предоставлять модуль gendiff с функцией
generate_diff().
Вызов этой функции возвращает строку с разницей между содержимым двух файлов.

Требования:

Сравниваются данные, а не строки файлов
Две строки дифа, которые отвечают за различия общего поля,
должны находиться рядом.
Причем сначала выводится строка, которая относится к первому файлу.
Затем выводится строка, которая относится ко второму файлу
(см. пример с timeout)
Результатом работы функции generate_diff() является строка
'''


# def main(first_file, second_file):
#     return 'Hello'


if __name__ == '__main__':
    generate_diff(args.first_file, args.second_file)
