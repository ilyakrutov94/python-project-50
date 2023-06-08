def gen_diff(container1, container2):
    keys = container1.keys() | container2.keys()
    result = dict()
    for key in keys:
        if key not in container1:
            result[key] = 'added'
        elif key not in container2:
            result[key] = 'deleted'
        elif container1[key] == container2[key]:
            result[key] = 'unchanged'
        else:
            value = 'changed'
            result[key] = value
    return result


print(gen_diff(
    {"one": "eon", "two": "two", "four": True},
    {"two": "own", "zero": 4, "four": True},
))
# {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}
