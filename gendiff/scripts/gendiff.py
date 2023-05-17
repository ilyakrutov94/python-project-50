#!/usr/bin/env python3
import json
import argparse

parser = argparse.ArgumentParser(description='Compares two configuration'
                                 ' files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()


def sorted_list_of_keys(dict1, dict2):
    list_of_keys1 = list(dict1.keys())
    list_of_keys1.sort()
    list_of_keys2 = list(dict2.keys())
    list_of_keys2.sort()
    return (list_of_keys1, list_of_keys2)


def string_creator(dict1, dict2):
    list_of_keys1, list_of_keys2 = sorted_list_of_keys(dict1, dict2)
    string = ''
    for keys1 in list_of_keys1:
        if keys1 not in list_of_keys2:
            string += ("- " + keys1 + ':'
                       + ' ' + str(dict1[keys1]) + '\n')
        elif keys1 in list_of_keys2:
            if dict1[keys1] == dict2[keys1]: # noqa
                string += ("  " + keys1 + ':'
                           + ' ' + str(dict1[keys1]) + '\n')
            elif dict1[keys1] != dict2[keys1]: # noqa
                string += ("- " + keys1 + ':'
                           + ' ' + str(dict1[keys1]) + '\n')
                string += ("+ " + keys1 + ':'
                           + ' ' + str(dict1[keys1]) + '\n')
    return string


def generate_diff(first_file, second_file):
    with open(first_file, 'r') as first_input:
        with open(second_file, 'r') as second_input:
            data1 = json.load(first_input)
            print(data1)
            data2 = json.load(second_input)
            print(data2)
            string = ""
            list_of_keys1 = list(data1.keys())
            list_of_keys1.sort()
            list_of_keys2 = list(data2.keys())
            list_of_keys2.sort()
            # print(list_of_keys1)
            # print(list_of_keys2)
            # for keys1 in list_of_keys1:
            #     print(keys1)
            #     if keys1 not in list_of_keys2:
            #         # string += "- " + keys1 + ':' + data1[keys1] + '\n'
            #         string += ("- " + keys1 + ':'
            #                    + ' ' + str(data1[keys1]) + '\n')
            #     elif keys1 in list_of_keys2:
            #         if data1[keys1] == data2[keys1]: # noqa
            #             string += ("  " + keys1 + ':'
            #                        + ' ' + str(data1[keys1]) + '\n')
            #         elif data1[keys1] != data2[keys1]: # noqa
            #             string += ("- " + keys1 + ':'
            #                        + ' ' + str(data1[keys1]) + '\n')
            #             string += ("+ " + keys1 + ':'
            #                        + ' ' + str(data2[keys1]) + '\n')
            print(string)
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
    # generate_diff(args.first_file, args.second_file)
    #     print(string_creator({
    #     "host": "hexlet.io",
    #     "timeout": 50,
    #     "proxy": "123.234.53.22",
    #     "follow": "false"
    #   }, {
    #     "timeout": 20,
    #     "verbose": "true",
    #     "host": "hexlet.io"
    #   }))
    pass
