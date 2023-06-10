from gendiff.formatters.format_json import make_json
from gendiff.formatters.format_plain import make_plain
from gendiff.formatters.format_stylish import make_stylish
from gendiff.diff_tree import build_diff_tree
from gendiff.file_parser import parse_file

FORMATTERS = {
    "stylish": make_stylish,
    "plain": make_plain,
    "json": make_json
}


def generate_diff(first_file: str, second_file: str,
                  formatter="stylish") -> str:
    '''
    Returns string with two compared json/yaml files.
    If function can't find file returns "Can't find {file path}"

        Parameters:
            first_file (str): Path to first json/yaml file
            second_file (str): Path to second json/yaml file
            formatter (str): Type of formatter

        Returns:
            compared_files (str): String with differences between files
    '''

    formatter_function = FORMATTERS[formatter]

    first_file = parse_file(first_file)
    second_file = parse_file(second_file)
    compared_files = build_diff_tree(first_file, second_file)
    styled_data = formatter_function(compared_files)

    return styled_data
