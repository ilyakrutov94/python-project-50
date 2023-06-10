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


def compare_dicts(source1, source2, final_key=''):
    all_keys = sorted(list(source1.keys() | source2.keys()))
    result = {}
    for key in all_keys:
        new_key = final_key + '.' + key if final_key else key
        if key not in source1:
            operation = 'added'
            new_value = source2[key]
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
            old_value = source2[key]
            result[new_key] = [operation, new_value, old_value]
        else:
            if isinstance(source1[key], dict) and\
                 isinstance(source2[key], dict):
                result.update(compare_dicts(source1[key],
                                            source2[key], new_key))
            else:
                operation = 'updated'
                new_value = source2[key]
                old_value = source1[key]
                result[new_key] = [operation, new_value, old_value]
    return result
