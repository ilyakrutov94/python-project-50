import itertools


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


def diff(source1, source2):
    all_keys = sorted(list(source1.keys() | source2.keys()))
    print("all_keys = ", all_keys)
    only_first = sorted(list(source1.keys() - source2.keys()))
    # print("only_before = ", only_first)
    only_second = sorted(list(source2.keys() - source1.keys()))
    # print("only_after = ", only_second)
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


def stringify(value, replacer='.', spaces_count=4):
    MOVEOUT = 2

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * (deep_indent_size - MOVEOUT)
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain('{', lines, [current_indent + "}"])
        return "\n".join(result)

    return iter_(value, 0)


text = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": "true",
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  }
}
# text2 = {
#     'common': "wow"
# }
   
print(stringify(diff(text1, text2)))
# print(stringify(text2))
