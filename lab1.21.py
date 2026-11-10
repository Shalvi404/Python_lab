import time
def dec(func):

    def wrapper(*args,**kwargs):
        start=time.perf_counter()
        result=func(*args,**kwargs)
        end=time.perf_counter()

        print(f"Время выполнения ф-ции:{end-start:.4f}")
        return result

    return wrapper
@dec
def power(x,y):
    time.sleep(3)
    print(x**y)
power(2,3)