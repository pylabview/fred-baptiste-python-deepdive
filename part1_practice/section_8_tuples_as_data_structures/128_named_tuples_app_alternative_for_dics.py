from collections import namedtuple

data_dict = dict(key1=1, key2=2, key3=3)

Data = namedtuple("Data", data_dict.keys())

data_list = [
    {"key1": 1, "key2": 2},
    {"key1": 1, "key2": 2},
    {"key1": 1, "key2": 2, "key3": 3},
    {"key2": 2},
]


def tuplefy_dicts(dicts):
    keys = sorted({key for dict_ in dicts for key in dict_.keys()})
    Struct = namedtuple("Struct", keys)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**d) for d in dicts]


if __name__ == "__main__":
    print("Named Tuples as alternative for dictionaries")
    print(data_dict)
    print(Data._fields)
    d1 = Data(*data_dict.values())
    print(d1)
    d2 = Data(**data_dict)
    print(d2)
    print(f"{getattr(d2, 'key4', None)}")
    print("Let's convert a list of dicts in and list of named tuples")
    print(data_list)
    print("Getting all keys from dict_list")
    keys = set()
    for d in data_list:
        for key in d.keys():
            keys.add(key)
    print(keys)
    # There is a better way to get the keys using set comprehension
    # 1. Get the unique keys form the target dict
    keys = {key for d in data_list for key in d.keys()}
    print(keys)
    # 2. Create the named tuple
    Struct = namedtuple("Struct", sorted(keys))
    # 3. Add None as default value
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    # 4. Now we have to iterate across the data_list
    # Then add the Struct to the list
    tuple_list = []
    for dict_ in data_list:
        tuple_list.append(Struct(**dict_))
    print(tuple_list)
    # Now let's create a general function
    print(tuplefy_dicts(data_list))
