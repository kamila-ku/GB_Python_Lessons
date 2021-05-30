my_list = input("Введите значение элементов через пробел ").split()
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)

# второй вариант кода (который исключаает ошибку с пробелом
# если пользователь введет цифры без него)

elements = int(input("Введите число элементов в списке "))
my_list = []
i = 0
pose = 0
e = 0
while i < elements:
   my_list.append(int(input("Введите значение ")))
   i += 1
print(my_list)
while e < len(my_list)//2:
   my_list[pose], my_list[pose + 1] = my_list[pose + 1], my_list[pose]
   pose += 2
   e = e + 1
print(my_list)