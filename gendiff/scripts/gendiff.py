#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description='Compares two configuration'
                                 ' files and shows a difference.')
parser.add_argument('-f', '--first_file', type=str, help='First file to compare') # noqa

parser.add_argument('-s', '--second_file', type=str, help='Second file to compare') # noqa
args = parser.parse_args()
# print(args.first_file)


def main():
    return 'Hello'


if __name__ == '__main__':
    main()
