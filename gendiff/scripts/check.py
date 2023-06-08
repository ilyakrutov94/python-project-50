#!/usr/bin/env python3
from gendiff.scripts.string_creator import sort_list_of_keys
import argparse
from gendiff.scripts.read import read_json


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                     ' files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str, help='set format of output') # noqa
    args = parser.parse_args()
    file1, file2 = read_json(args.first_file, args.second_file)
    print(sort_list_of_keys(file1, file2))
    return sort_list_of_keys(file1, file2)
