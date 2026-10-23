def merge_dicts(dict1, dict2):
    for key,value in dict2.items():
        if key in dict1:
            type1=type(dict1[key])
            type2=type(value)
            if type1==dict and type2==dict:
                merge_dicts(dict1[key], value)
            elif (type1==list and type2==list) or (type1==tuple and type2==tuple):
                dict1[key]=dict1[key]+value
            elif type1==set and type2==set:
                dict1[key]=dict1[key]|value
            else:
                dict1[key]=coping(value)
        else:
            dict1[key]=coping(value)
def coping(thing):
    type_thing=type(thing)
    if type_thing==dict:
        return{k:coping(v) for k,v in thing.items()}
    elif type_thing==list:
        return[coping(v) for v in thing]
    elif type_thing==set:
        return set(thing)
    elif type_thing==tuple:
        return tuple(coping(v) for v in thing)
    return thing
dict1 = {"a": 1, "b": {"c": 1, "f": 4}}
dict2 = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict1,dict2)
print(dict1)