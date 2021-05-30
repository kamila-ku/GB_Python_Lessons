earnings = int(input("Напишите значение выручки "))
costs = int(input("Напишите значение издержек "))
if earnings > costs:
    print("Фирма работает с прибылью. Рентабельность выручки составила ", earnings/costs)
    workers = int(input("Введите количество сотрудников "))
    print("Прибыль фирмы на одного сотрудника составила ", earnings/workers)
elif earnings == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")