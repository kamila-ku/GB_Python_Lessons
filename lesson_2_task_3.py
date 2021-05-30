month = int(input("Введите номер месяца "))
seasons_dict = {1 : "'осень'", 2 : "'лето'", 3 : "'весна'", 4 : "'зима'"}
seasons_list = ["Зима", "Весна", "Лето", "Осень"]
if month == 1 or month == 2 or month == 12:
    print("Месяц находится в сезоне", seasons_dict.get(4))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print("Месяц находится в сезоне", seasons_dict.get(3))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print("Месяц находится в сезоне", seasons_dict.get(2))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print("Месяц находится в сезоне", seasons_dict.get(1))
    print(seasons_list[3])
else:
    print("Попробуйте еще раз!")
