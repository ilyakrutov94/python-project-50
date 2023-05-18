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
                           + ' ' + str(dict2[keys1]) + '\n')
    for keys2 in list_of_keys2:
        if keys2 not in list_of_keys1:
            string += ("+ " + keys2 + ':'
                       + ' ' + str(dict2[keys2]) + '\n')
    return string


def generate_diff(first_file, second_file):
    with open(first_file, 'r') as first_input:
        with open(second_file, 'r') as second_input:
            data1 = json.load(first_input)
            data2 = json.load(second_input)
            string = string_creator(data1, data2)
            # print(string)
    return string


if __name__ == '__main__':
    generate_diff(args.first_file, args.second_file)
