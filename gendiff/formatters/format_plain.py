import json
from gendiff.constants import (
    ADDED,
    UPDATED,
    REMOVED,
    UNCHANGED,
    NESTED,
    TYPE,
    VALUE,
    OLD_VAL,
    NEW_VAL,
    CHILDREN
)


def make_plain(diff_tree, parent_key=''):
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
    result = ''
    items_diff = diff_tree.items()
    if diff_tree:
        lines = []
    # items_diff = {added_key: {TYPE: ADDED, VALUE: source2.get(added_key)}}
    for elem in items_diff:
        _, item_value = elem
    # items_value = {TYPE: ADDED, VALUE: source2.get(added_key)}
        if item_value.get(TYPE) != UNCHANGED:
            lines.append(stringify_node(elem, parent_key))

        result = '\n'.join(lines)
    return result


def stringify_node(item, parent_key=''):

    current_key, item_value = item

    item_type = item_value.get(TYPE)
    key = f"{parent_key}.{current_key}" if parent_key else current_key

    if item_type == NESTED:
        children = item_value.get(CHILDREN)
        children_diff = children.items()
        lines = []
        for child in children_diff:
            _, child_value = child
            if child_value.get(TYPE) != UNCHANGED:
                lines.append(stringify_node(child, key))

            items_children = '\n'.join(lines)
        return items_children

    if item_type == UPDATED:
        value1 = item_value.get(OLD_VAL)
        value2 = item_value.get(NEW_VAL)
        old_value = _format_value(value1)
        new_value = _format_value(value2)
        item_str = f"Property '{key}' was updated. From {old_value} to {new_value}" # noqa
        return item_str

    if item_type == REMOVED:
        item_str = f"Property '{key}' was removed"
        return item_str

    if item_type == ADDED:
        value = item_value.get(VALUE)
        val = _format_value(value)
        item_str = f"Property '{key}' was added with value: {val}"
        return item_str


def _format_value(value):
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
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        if value is None or isinstance(value, bool):
            return json.dumps(value)
        else:
            return value
