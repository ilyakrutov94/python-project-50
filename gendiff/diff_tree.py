#!/usr/bin/env python3

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


def build_diff_tree(source1, source2):
    '''
    Building difference tree for further render.
    Format {added_key: {TYPE: ADDED, VALUE: source2.get(added_key)}}
    '''
    result = {}
    set1 = set(source1)
    set2 = set(source2)
    common_keys = set1 & set2
    # common_keys are keys common both to source1 and source2
    added_keys = set2 - set1
    # added_keys are keys that unique to source2
    deleted_keys = set1 - set2
    # added_keys are keys that unique to source1
    for added_key in added_keys:
        result[added_key] = {
            TYPE: ADDED,
            VALUE: source2.get(added_key)
        }
    # {added_key: {TYPE: ADDED, VALUE: source2.get(added_key)}}
    for deleted_key in deleted_keys:
        result[deleted_key] = {
            TYPE: REMOVED,
            VALUE: source1.get(deleted_key)
        }

    for common_key in common_keys:
        old_value = source1.get(common_key)
        new_value = source2.get(common_key)
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            result[common_key] = {
                TYPE: NESTED,
                CHILDREN: build_diff_tree(old_value, new_value)
            }
    # starting recursion
        else:
            result[common_key] = {
                TYPE: UPDATED,
                OLD_VAL: old_value,
                NEW_VAL: new_value
            }

        if old_value == new_value:
            result[common_key] = {
                TYPE: UNCHANGED,
                VALUE: old_value
            }

    sorted_result = dict(sorted(result.items(), key=lambda k: k))
    return sorted_result
