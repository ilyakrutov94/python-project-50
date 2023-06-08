def stringify(value, replacer=' ', spaces_count=1):
    if type(value) == dict:
        string = ''
        for key, val in value.items():
            if type(val) == str or type(val) == int or type(val) == bool:
                string += replacer*spaces_count + f"{key}: " + str(val) + "\n"
            else:
                dop = (f"{key}: " +
                       stringify(val, replacer, spaces_count) + "\n")
                list = dop.split('\n')
                new_list = []
                for item in list:
                    if item:
                        item = replacer*spaces_count + item
                    new_list.append(item)
                string += '\n'.join(new_list)
        full_string = "{\n" + string + "}"
        return full_string
    else:
        string = replacer*spaces_count + str(value)
        return string


data = {
    "hello": "world",
    "is": True,
    "nested":
        {"count": 5}
        }
data2 = {
    "hello": "world",
    "is": True,
    "nested":
        {"count":
            {"key": 5}
         }
        }
