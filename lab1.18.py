import datetime
def log_calls(file_txt):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            start=datetime.datetime.now()
            form_start=start.strftime("%d %b %H:%M:%S")
            arguments=f"{args},{kwargs}"
            with open(file_txt,"a",encoding="utf-8") as file:
                file.write(f"Функция:{function.__name__},время вызова:{form_start},аргументы:{arguments}\n")
            return result
        return wrapper
    return decorator
file="file.txt"
@log_calls(file)
def add(a,b):
    return a+b
add(23,13)
with open("file.txt","r",encoding="utf-8") as file:
    print(file.read())


