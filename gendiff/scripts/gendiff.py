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


def generate_diff_plain(first_file, second_file):
    if first_file.endswith('json'):
        data1, data2 = read_json(first_file, second_file)
        string = diff_plain(data1, data2)
        return stringify_plain(string)
    elif first_file.endswith('yaml') or first_file.endswith('yml'):
        data1, data2 = read_yaml(first_file, second_file)
        string = diff_plain(data1, data2)
        return stringify_plain(string)
    else:
        return ('Wrong file format')


def generate_diff_json(first_file, second_file):
    if first_file.endswith('json'):
        data1, data2 = read_json(first_file, second_file)
        string = diff(data1, data2)
        return json.dumps(string, indent=4)
    else:
        return ('Wrong file format')


def generate_diff_raw(first_file, second_file):
    if first_file.endswith('json'):
        data1, data2 = read_json(first_file, second_file)
        string = diff(data1, data2)
        return string
    elif first_file.endswith('yaml') or first_file.endswith('yml'):
        data1, data2 = read_yaml(first_file, second_file)
        string = diff(data1, data2)
        return string
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


def diff_plain(source1, source2, final_key=''):
    all_keys = sorted(list(source1.keys() | source2.keys()))
    result = {}
    for key in all_keys:
        if final_key:
            new_key = final_key + '.' + key
        else:
            new_key = key
        if key not in source1:
            operation = 'added'
            new_value = source2[key]
            if isinstance(new_value, dict):
                new_value = '[complex value]'
            old_value = ''
            result[new_key] = [operation, new_value, old_value]
        elif key not in source2:
            operation = 'removed'
            new_value = ''
            old_value = ''
            result[new_key] = [operation, new_value, old_value]
        elif source1[key] == source2[key]:
            operation = 'unchanged'
            new_value = source2[key]
            if isinstance(new_value, dict):
                new_value = '[complex value]'
            old_value = source2[key]
            if isinstance(old_value, dict):
                old_value = '[complex value]'
            result[new_key] = [operation, new_value, old_value]
        else:
            if isinstance(source1[key], dict) and\
                 isinstance(source2[key], dict):
                result.update(diff_plain(source1[key], source2[key], new_key))
            else:
                operation = 'updated'
                new_value = source2[key]
                if isinstance(new_value, dict):
                    new_value = '[complex value]'
                old_value = source1[key]
                if isinstance(old_value, dict):
                    old_value = '[complex value]'
                result[new_key] = [operation, new_value, old_value]
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


def stringify_plain(value):
    convert = {False: 'false',
               None: 'null',
               True: 'true'
               }
    exceptions = ("false", "null", "true", "[complex value]")
    lines = []
    for key, value in value.items():
        if value[0] == 'added':
            new_value = value[1]
            if new_value in convert:
                new_value = convert[new_value]
            if new_value in exceptions:
                lines.append(f"Property '{key}' was added "
                             f"with value: {new_value}")
            else:
                lines.append(f"Property '{key}' was added "
                             f"with value: '{new_value}'")
        if value[0] == 'removed':
            lines.append(f"Property '{key}' was removed")
        if value[0] == 'updated':
            old_value = value[2]
            new_value = value[1]
            if new_value in convert:
                new_value = convert[new_value]
            if old_value in convert:
                old_value = convert[old_value]
            if new_value in exceptions and old_value not in exceptions:
                lines.append(f"Property '{key}' was updated. "
                             f"From '{old_value}' to {new_value}")
            elif old_value in exceptions and new_value not in exceptions:
                lines.append(f"Property '{key}' was updated. "
                             f"From {old_value} to '{new_value}'")
            elif old_value and new_value in exceptions:
                lines.append(f"Property '{key}' was updated. "
                             f"From {old_value} to {new_value}")
            else:
                lines.append(f"Property '{key}' was updated. "
                             f"From '{old_value}' to '{new_value}'")
    return "\n".join(lines)
# rendering SECTION END
