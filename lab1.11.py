try:
    age = int(input(f"Возраст: "))
    pay = float(input(f"Доход: "))
    credit = float(input(f"Сумма кредита: "))
    time = int(input(f"Срок(месяцы): "))
    history = input(f"Кредитная история (отличная, хорошая, удовлетворительная, плохая):").strip().lower()
    is_helper = input(f"Есть поручители? (да/нет): ").strip().lower() == "да"
    is_money = input(f"Есть залог? (да/нет): ").strip().lower() == "да"
    coefficient=credit/pay
    if history=="плохая" or age<18 or age>70:
        recommendation="Не одобрять кредит"
        risk="Критический"
        stavka="Нету"
    elif (history=="удовлетворительная" or coefficient>5) and not is_helper and not is_money:
        recommendation = "Одобрить кредит, но клиент высокого уровня риска(посоветовать найти залог и поручателя)"
        risk = "Высокий"
        stavka ="40%"
    elif (history=="удовлетворительная" or coefficient>5) and (is_helper or  is_money):
        recommendation = "Одобрить кредит, но клиент среднего уровня риска"
        risk = "Средний"
        stavka = "30%"
    elif (history=="хорошая" or history=="отличная") and (coefficient>5):
        recommendation = "Одобрить кредит, но клиент среднего уровня риска(посоветовать найти залог или поручателя)"
        risk = "Средний"
        stavka = "30%"
    elif (history=="хорошая" or history=="отличная") and ((is_helper or is_money) or coefficient<=5):
        recommendation = "Одобрить кредит, идеальный клиент"
        risk = "Низкий"
        stavka = "20%"
    else:
        recommendation = "Неизвестно, узнать о клиенте больше инфрмации и принять решение сотруднику"
        risk = "Неизвестно"
        stavka = "0%"
    print(f"Соотношение кредит/доход: {coefficient:.2f}")
    print(f"Категория риска: {risk}")
    print(f"Предложенная ставка: {stavka}")
    print(f"Решение: {recommendation}")
except ValueError:
    print(f"Неверный набор данных")