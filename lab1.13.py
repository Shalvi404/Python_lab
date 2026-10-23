
try:
   text=input(f"Введите числа через пробел:").split()
   num=[float(n) for n in text]
   unique_num=set(num)
   print(f"Уникальные числа{unique_num}")
   sum=0
   again_num=[]
   ch_num=[]
   notch_num=[]
   neg_num=[]
   float_num=[]
   for nums in unique_num:
       if num.count(nums)>=2:
           again_num.append(nums)
       if nums%2==0:
           ch_num.append(nums)
       elif nums%2!=0:
           notch_num.append(nums)
       if nums<0:
           neg_num.append(nums)
       if nums-int(nums)!=0:
           float_num.append(nums)
       if nums%5==0:
           sum+=nums
   print(f"Повторяющиеся числа:{again_num}")
   print(f"Четные числа:{ch_num}")
   print(f"Нечетные числа:{notch_num}")
   print(f"Отрицательные числа:{neg_num}")
   print(f"Вещественные числа:{float_num}")
   print(f"Сумма кратных 5:{sum}")
except:
    print(f"Неверно выбраны числа")