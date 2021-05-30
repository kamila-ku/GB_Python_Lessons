my_str = str(input("Введите несколько слов: "))
my_list = my_str.split()
i = 1
el = ()
for el in (my_list):
    if len(str(el)) <= 10:
        print(i, el)
        i = i + 1
    else:
        print(i, el [0:10])
        i = i + 1