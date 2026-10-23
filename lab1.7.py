minutes=int(input(f"Введите кол-во израсходованных минут:"))
sms=int(input(f"Введите кол-во израсходованных sms:"))
tra=int(input(f"Введите кол-во израсходованного трафика в МБ:"))
base_cost=24.99
fin_cost=base_cost
print(f"Базовая цена за тариф:{base_cost:.2f} рублей")
if minutes-60>0:
    delta_minutes=(minutes-60)*0.89
    print(f"Цена за доп. минуты:{delta_minutes} рублей")
    fin_cost+=delta_minutes
if sms-30>0:
    delta_sms=(sms-30)*0.59
    print(f"Цена за доп. sms:{delta_sms} рублей")
    fin_cost+=delta_sms
if tra-1024>0:
    delta_tra=(tra-1024)*0.79
    print(f"Цена за доп. трафик:{delta_tra} рублей")
    fin_cost+=delta_tra
nalog=fin_cost*0.02
print(f"Налог:{nalog:.2f} рублей")
fin_cost+=nalog
print(f"Финальная стоимость:{fin_cost:.2f} рублей")


