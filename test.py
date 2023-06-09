def diff_plain(source1, source2, final_key=''):
    all_keys = sorted(list(source1.keys() | source2.keys()))
    result = {}
    for key in all_keys:
        if key not in source1:
            operation = 'added'
            add_value = source2[key]
            update_value = ''
            final_key += key
            result[final_key] = [operation, add_value, update_value]
    return result


text1 = {
    "common": {
        "setting1": "Value 1",
    },
    'abuse': 'smth',
    'glacier': 'dirty',
    'agony': 'dirty'
    }

text2 = {
    "common2": {
        "setting2": "Value 1",
    },
    "common": {
        "setting1": "Value 3",
        "setting2": {"dasdas": "dsadasd"}
    },
    'abuse': 'smth',
    'glacier': 'clean',
    'text2_unique': 'gold'
    }

print(diff_plain(text1, text2))
