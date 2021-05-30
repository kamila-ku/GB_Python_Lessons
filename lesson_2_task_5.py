my_list = [8, 4, 3, 3, 1]
print(my_list)
new_element = int(input("Введите любую цифру от 0 до 9 "))
my_list.append(new_element)
my_list.sort(reverse = True)
print(my_list)

# Понимаю, что возможно это не совсем то, что необходимо, но под условия задачи это подходит и сортирует по логике.
# Если мы принимаем, что не возрастающий список == убывающий (что не совсем так), то работает идеально:)
# Последовательность чисел в функции идет от большего к меньшему, дублируя повторяющийеся числа
# (поэтому она не убывающая, но логику кода это вроде бы не нарушает)

number = int(input("Введите новый элемент рейтинга "))
my_list = [7, 5, 3, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

# Скорее всего, надо было сделат что-то подобное...
# Просто и первый вариант работает)