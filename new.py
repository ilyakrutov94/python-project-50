import json
import itertools
data = {'common.follow': ['added', False, '', 'follow'],
        'common.setting1': ['unchanged', 'Value 1', 'Value 1', 'setting1'],
        'common.setting2': ['removed', '', 200, 'setting2'],
        'common.setting3': ['updated', None, True, 'setting3'],
        'common.setting4': ['added', 'blah blah', '', 'setting4'],
        'common.setting5': ['added',
                            {'key5': 'value5'}, '', 'setting5'],
        'common.setting6.doge.wow': ['updated', 'so much', '', 'wow'],
        'common.setting6.key': ['unchanged', 'value', 'value', 'key'],
        'common.setting6.ops': ['added', 'vops', '', 'ops'],
        'group1.baz': ['updated', 'bars', 'bas', 'baz'],
        'group1.foo': ['unchanged', 'bar', 'bar', 'foo'],
        'group1.nest': ['updated', 'str',
                        {'key': 'value'}, 'nest'],
        'group2': ['removed', '',
                   {'abc': 12345, 'deep': {'id': 45}}, 'group2'],
        'group3': ['added',
                   {'deep': {'id': {'number': 45}}, 'fee': 100500},
                   '', 'group3']}
data2 = {'group2': ['removed', '',
                    {'abc': 12345, 'deep': {'id': 45}}, 'group2'],
         'group3': ['added',
                    {'deep': {'id': {'number': 45}}, 'fee': 100500},
                    '', 'group3']}
DEFAULT_INDENT = 4
TYPES_TO_INDENTS = {
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    ',
    'nested': '    '}


def stringify_value(value, level):
    if not isinstance(value, dict):
        if value is None or isinstance(value, bool):
            return json.dumps(value)
        else:
            return value
    indent = get_indent(level)
    lines = []
    for key, val in value.items():
        lines.append(f'{indent}    {key}: {stringify_value(val, level+1)}')
    result = itertools.chain('{', lines, [indent + '}'])
    return '\n'.join(result)


def get_indent(level):
    indent = level * DEFAULT_INDENT * ' '
    return indent


def stringify_node(item, level=0):
    indent = get_indent(level)
    key, item_value = item
    item_type = item_value.get(TYPE)

    if item_type == NESTED:
        children = item_value.get(CHILDREN)
        new_lines = [
            stringify_node(child, level + 1)
            for child in list(children.items())
        ]
        child_str = '{\n' + '\n'.join(new_lines) + '\n'+ indent + TYPES_TO_INDENTS['nested'] + '}'
        item_str = f"{indent}    {key}: {child_str}"
        return item_str

    if item_type == UPDATED:
        value1 = item_value.get(OLD_VAL)
        value2 = item_value.get(NEW_VAL)
        val1 = stringify_value(value1, level + 1)
        val2 = stringify_value(value2, level + 1)
        res_str1 = f"{indent}{TYPES_TO_INDENTS['removed']}{key}: {val1}"
        res_str2 = f"{indent}{TYPES_TO_INDENTS['added']}{key}: {val2}"
        item_str = res_str1 + '\n' + res_str2
        return item_str

    value = item_value.get(VALUE)
    val = stringify_value(value, level + 1)

    if item_type == 'unchanged':
        return f"{indent}{TYPES_TO_INDENTS['unchanged']}{key}: {val}"

    if item_type == 'removed':
        item_str = f"{indent}{TYPES_TO_INDENTS['removed']}{key}: {val}"
        return item_str

    if item_type == 'added':
        item_str = f"{indent}{TYPES_TO_INDENTS['added']}{key}: {val}"
        return item_str


def make_stylish(value: dict,
                 replacer: str = '.',
                 spaces_count: int = 4) -> str:
    '''
    Returns json-like output from diffence_dict
    If key: value is equal in both files - returns:
        "{COMMON} {key: value}"
    If key: value is different in first and second files - returns:
        "{IN_FIRST_FILE} {key1: value1}"
        "{IN_SECOND_FILE} {key2: value2}"
    '''
    MOVEOUT = 2

    lines = []
    for path, value in value.items():
        path_head, path_sign, path_tail = path.partition('.')
        operation = value[0]
        new_value = value[1]
        old_value = value[2]
        key = value[3]
        deep_indent_size = 0 + spaces_count
        deep_indent = replacer * (deep_indent_size - MOVEOUT)
        if path_sign == '':
            line = f'{deep_indent}..{path_head}: {_support(new_value, deep_indent_size)}' # noqa


def _support(path_head, path_sign, path_tail,
             operation, new_value, current_value,
             old_value, key, depth=0):
    if not isinstance(current_value, dict):
        return _convert_bool_json(current_value)


def _convert_bool_json(source: str) -> str:
    '''
    converts False, None, True in Python
    to false, null, true in json
    '''
    if isinstance(source, bool) or source is None:
        return {
            False: 'false',
            True: 'true',
            None: 'null',
        }.get(source)
    return source


print(make_stylish(data2))

result = ('path_head: ', 'group2',
          'path_sign: ', '',
          'path_tail: ', '',
          'operation: ', 'removed',
          'new_value: ', '',
          'value: ', ['removed', '', {'abc': 12345, 'deep': {'id': 45}},
                      'group2'],
          'old_value: ', {'abc': 12345, 'deep': {'id': 45}},
          'key: ', 'group2')
