import itertools


def make_stylish(value: dict,
                 replacer: str = ' ',
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

    def iter_(current_value, depth: int = 0):
        if not isinstance(current_value, dict):
            return _convert_bool_json(current_value)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * (deep_indent_size - MOVEOUT)
        current_indent = replacer * (depth)
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain('{', lines, [current_indent + "}"])
        return "\n".join(result)

    return iter_(value, 0)


def _convert_bool_json(source: str) -> str:
    '''
    converts False, None, True in Python
    to false, null, true in json
    '''
    CONVERT = {False: 'false',
               None: 'null',
               True: 'true'
               }
    if source in CONVERT:
        return CONVERT[source]
    return source
