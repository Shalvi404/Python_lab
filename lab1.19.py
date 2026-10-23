def cache(func):
    cache={}
    def wrapper(*args,**kwargs):
        key=(args,frozenset(kwargs.items()))
        if key in cache:
            print(f"обнаружен cache{key}")
            return cache[key]
        result = func(*args,**kwargs)
        cache[key]=result
        return result
    return wrapper
@cache
def multi(a):
    print(a)
multi((1,2,3))
multi((1,2,3))



