koef={
    "масса":{"мг":1e-6,"г":1e-3,"кг":1,"тонны":1e3},
    "длина":{"мм":1e-3,"см":1e-2,"м":1,"км":1e3},
    "объем":{"мл":1e-3,"л":1,"м3:1":1e3}
}
def get_input(prompt, valid_keys):
    while True:
        val = input(prompt).lower().strip()
        if val in valid_keys:
            return val
        print(f"Ошибка! Доступно: {list(valid_keys)}")
categ=get_input(f"Введитe название физ. величины {list(koef)}: ", koef.keys())
unit_in=get_input(f"Введитe название первоначальной единицы {list(koef[categ])}: ", koef[categ].keys())
unit_out=get_input(f"Введитe название единицы, в которую нужно перевести {list(koef[categ])}: ", koef[categ].keys())
value=float(input(f"Значение в {unit_in}:"))
result=value*koef[categ][unit_in]/koef[categ][unit_out]
print(f"Переведено из {value}{unit_in} в {result}{unit_out}")