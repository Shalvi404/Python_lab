import random
rand_digit=random.randint(1,100)
digit=-1
while rand_digit!=digit:
    digit=int(input(f"Введите число от 1 до 100:"))
    if rand_digit>digit:
        print('>')
    elif rand_digit==digit:
        break
    else:
        print('<')
print(f"Молодец,ты выйграл!")