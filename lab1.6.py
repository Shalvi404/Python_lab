month=int(input(f"Введите месяц рождения(1-12):"))
day=int(input(f"Введите день рождения(1-31):"))
if (day>=20 and month==1) or (day<=18 and month==2):
      print(f"Вы водолей")
elif (day>=19 and month==2) or (day<=20 and month==3):
    print(f"Вы рыбы")
elif (day>=21 and month==3) or (day<=19 and month==4):
    print(f"Вы овен")
elif (day>=20 and month==4) or (day<=20 and month==5):
    print(f"Вы телец")
elif (day>=21 and month==5) or (day<=20 and month==6):
    print(f"Вы близнец")
elif (day>=21 and month==6) or (day<=22 and month==7):
    print(f"Вы рак")
elif (day>=23 and month==7) or (day<=22 and month==8):
    print(f"Вы лев")
elif (day>=23 and month==8) or (day<=22 and month==9):
    print(f"Вы дева")
elif (day>=23 and month==9) or (day<=22 and month==10):
    print(f"Вы весы")
elif (day>=23 and month==10) or (day<=21 and month==11):
    print(f"Вы скорпион")
elif (day >= 22 and month == 11) or (day <= 21 and month == 12):
    print(f"Вы стрелец")
elif (day >= 22 and month == 12) or (day <= 19 and month == 1):
    print(f"Вы козерог")
else:
    print(f"Неправильная дата")
