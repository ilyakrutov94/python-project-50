#!/usr/bin/env python3
from gendiff.cli import args
from gendiff.generate_diff import generate_diff


def main():
    difference = generate_diff(args.first_file, args.second_file,
                               args.format)
    print(difference)


if __name__ == "__main__":
    main()
