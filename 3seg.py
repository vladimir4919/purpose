#создаем первый список
a_enter_first=[]
for i in range(int(input('ввести цифру'))):
    a_enter_first.append(int(input()))

#сортируем первый список
a_enter_first.sort()
print(a_enter_first)
#создаем второй список
a_enter_second=[]
for i in range(int(input('ввести цифру'))):
    a_enter_second.append(int(input()))
#сортируем второй список
a_enter_second.sort()
print(a_enter_second)
# по числам в первом списке
#считаем сколько раз это число входит
#во второй список и в цикле удаляем из второго списка
for elem in a_enter_first:
    while a_enter_second.count(elem) != 0:
        a_enter_second.remove(elem)
print(a_enter_second)