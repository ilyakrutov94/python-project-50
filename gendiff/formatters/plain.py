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
        new_value = _get_value(value[1])
        old_value = _get_value(value[2])
        if operation == 'added':
            if new_value in EXCEPTIONS:
                lines.append(f"Property '{path}' was added "
                             f"with value: {new_value}")
            else:
                lines.append(f"Property '{path}' was added "
                             f"with value: {new_value}")
        if operation == 'removed':
            lines.append(f"Property '{path}' was removed")
        if operation == 'updated':
            lines.append(f"Property '{path}' was updated. "
                         f"From {old_value} to {new_value}")
    return "\n".join(lines)


def _get_value(value):
    '''
    converts dict_values into:
    1) '[complex value]' for dict;
    2) false, true for bool;
    3) null for None;
    4) value without '' for int
    5) 'value' for others
    '''
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool) or value is None:
        return {
            False: 'false',
            True: 'true',
            None: 'null',
        }.get(value)
    if isinstance(value, int) or isinstance(value, list):
        return value
    return f'\'{value}\''
