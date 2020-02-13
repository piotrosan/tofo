

def collapse_complex_key(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        master_key, *sub_key = key.split('.')
        if not sub_key:
            new_dict[master_key] = value
            continue
        new_dict.setdefault(master_key, {})
        new_dict[master_key][sub_key.pop()] = value
    return new_dict
