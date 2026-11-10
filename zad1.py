def logs_exe(text_txt):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(text_txt,'a',encoding='utf-8') as file:

                for k,v in list_kkal.items():
                    file.write(f"{k}--{v}\n")
                for k,v in kkal_spent.items():
                    file.write(f"{k}--{v}\n")
                file.write(res)
            return res
        return wrapper
    return decorator
list_kkal={}
kkal_spent={}
n=1
i=1
while n!=0:
    eda = input("ВВедите еду которую съели:")
    kkal_gain = int(input("ВВедите kkal за еду которую съели:"))
    list_kkal[eda]=kkal_gain
    n = int(input("1-продолжить, 0-выйти:"))
while i != 0:
    exec = input("ВВедите упражнение:")
    kkal_lose = int(input("ВВедите kkal которую потратили:"))
    kkal_spent[exec] = kkal_lose
    i = int(input("1-продолжить, 0-выйти:"))

@logs_exe("product.txt")
def calculate():
    all_eaten_kkal=0
    for eda in list_kkal:
        all_eaten_kkal+=list_kkal[eda]
    all_spent_kkal=0
    for exec in kkal_spent:
        all_spent_kkal+=kkal_spent[exec]
    if all_eaten_kkal-all_spent_kkal>2500:
        return f"Вам надо больше заниматься, еще сбросить {all_eaten_kkal-all_spent_kkal-2500}\n"
    else:
        return "Все good\n"
calculate()

