def make_plain(value: dict) -> str:
    '''
    Returns plain output from diffence_dict
    If path: value doesnt change - returns nothing
    If path: value changed in second file - returns:
        "Property {path} was updated. From {old_value} to {new_value}"
    If path: value is only in second value - returns:
        "Property {path} was added with value: {new_value}
    If path: value is only in first file - returns:
        "Property {path} was removed"
    '''
    EXCEPTIONS = ("false", "null", "true", "[complex value]")
    lines = []
    for path, value in value.items():
        operation = value[0]
        new_value = _convert_bool_json(_convert_complex(value[1]))
        old_value = _convert_bool_json(_convert_complex(value[2]))
        if operation == 'added':
            if new_value in EXCEPTIONS:
                lines.append(f"Property '{path}' was added "
                             f"with value: {new_value}")
            else:
                lines.append(f"Property '{path}' was added "
                             f"with value: '{new_value}'")
        if operation == 'removed':
            lines.append(f"Property '{path}' was removed")
        if operation == 'updated':
            if new_value in EXCEPTIONS and old_value not in EXCEPTIONS:
                lines.append(f"Property '{path}' was updated. "
                             f"From '{old_value}' to {new_value}")
            elif old_value in EXCEPTIONS and new_value not in EXCEPTIONS:
                lines.append(f"Property '{path}' was updated. "
                             f"From {new_value} to '{new_value}'")
            elif old_value and new_value in EXCEPTIONS:
                lines.append(f"Property '{path}' was updated. "
                             f"From {old_value} to {new_value}")
            else:
                lines.append(f"Property '{path}' was updated. "
                             f"From '{old_value}' to '{new_value}'")
    return "\n".join(lines)


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


def _convert_complex(source: str | list) -> str:
    '''
    converts dict_values into '[complex value]'
    '''
    if isinstance(source, dict):
        return '[complex value]'
    return source
