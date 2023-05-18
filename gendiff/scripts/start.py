from gendiff.scripts.gendiff import generate_diff
import argparse


def start(path1, path2):
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                     ' files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str, help='set format of output') # noqa
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))
    return generate_diff(args.first_file, args.second_file)