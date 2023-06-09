from gendiff.scripts.gendiff import generate_diff_stylish,\
    generate_diff_plain, generate_diff_raw, generate_diff_json
import argparse
parser = argparse.ArgumentParser(description='Compares two configuration'
                                 ' files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format',
                    type=str,
                    choices=['stylish', 'raw', 'plain', 'json'],
                    default='stylish',
                    help='set format of output') # noqa
args = parser.parse_args()
stylish = generate_diff_stylish(args.first_file, args.second_file)
raw = generate_diff_raw(args.first_file, args.second_file)
plain = generate_diff_plain(args.first_file, args.second_file)
json = generate_diff_json(args.first_file, args.second_file)


def start():
    if args.format == 'stylish':
        return stylish
    elif args.format == "plain":
        return plain
    elif args.format == "json":
        return json
    else:
        return raw
