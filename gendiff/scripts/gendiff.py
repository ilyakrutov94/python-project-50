#!/usr/bin/env python3
import json
import yaml
import itertools


# READ SECTION START
def read_json(first_file, second_file):
    with open(first_file, 'r') as first_input:
        with open(second_file, 'r') as second_input:
            data1 = json.load(first_input)
            data2 = json.load(second_input)
    return (data1, data2)


def read_yaml(first_file, second_file):
    with open(first_file, 'r') as first_input:
        with open(second_file, 'r') as second_input:
            data1 = yaml.load(first_input, Loader=yaml.FullLoader)
            data2 = yaml.load(second_input, Loader=yaml.FullLoader)
    return (data1, data2)
# READ SECTION END


# diff generation SECTION START
def generate_diff(first_file, second_file):
    if first_file.endswith('json'):
        data1, data2 = read_json(first_file, second_file)
        string = create_string(data1, data2)
        return string
    elif first_file.endswith('yaml') or first_file.endswith('yml'):
        data1, data2 = read_yaml(first_file, second_file)
        string = create_string(data1, data2)
        return string
    else:
        return ('Wrong file format')


def generate_diff_stylish(first_file, second_file):
    if first_file.endswith('json'):
        data1, data2 = read_json(first_file, second_file)
        string = diff(data1, data2)
        return stringify(string)
    elif first_file.endswith('yaml') or first_file.endswith('yml'):
        data1, data2 = read_yaml(first_file, second_file)
        string = diff(data1, data2)
        return stringify(string)
    else:
        return ('Wrong file format')
# diff generation SECTION END


# diff calculate SECTION START
def diff(source1, source2):
    all_keys = sorted(list(source1.keys() | source2.keys()))
    result = {}
    for key in all_keys:
        if key not in source1:
            result[('+ ' + key)] = source2[key]
        elif key not in source2:
            result[('- ' + key)] = source1[key]
        elif source1[key] == source2[key]:
            result[('  ' + key)] = str(source1[key])
        else:
            if type(source1[key]) == dict and type(source2[key]) == dict:
                result[('  ' + key)] = diff(source1[key], source2[key])
            else:
                result[('- ' + key)] = source1[key]
                result[('+ ' + key)] = source2[key]
    return result


def sort_list_of_keys(dict1, dict2):
    list_of_keys1 = list(dict1.keys())
    list_of_keys1.sort()
    list_of_keys2 = list(dict2.keys())
    list_of_keys2.sort()
    return (list_of_keys1, list_of_keys2)


def create_string(dict1, dict2):
    list_of_keys1, list_of_keys2 = sort_list_of_keys(dict1, dict2)
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
    return string[:-1]
# diff calculate SECTION END


# rendering SECTION START
def stringify(value, replacer='.', spaces_count=4):
    MOVEOUT = 2
    convert = {False: 'false',
               None: 'null',
               True: 'true'
               }

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            if current_value in convert:
                return convert[current_value]
            else:
                return str(current_value)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * (deep_indent_size - MOVEOUT)
        current_indent = replacer * (depth)
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain('{', lines, [current_indent + "}"])
        return "\n".join(result)

    return iter_(value, 0)
# rendering SECTION END
