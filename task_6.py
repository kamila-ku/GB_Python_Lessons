a = int(input ("Введите пройденное количество км "))
b = int(input("Введите сколько еще пробежать км "))
day = 1
all_km = a
while all_km < b:
    a = a + 0.1 * a
    day += 1
    all_km = all_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % day)

