a_enter=[]
for i in range(int(input('ввести цифру'))):
    a_enter.append(int(input()))
a_enter.sort()

for elem in a_enter:
    while a_enter.count(elem) > 1:
        a_enter.remove(elem)
for elem in a_enter:
    print(elem, end='/')
   # print(elem, end=':')
    #print(elem, end=';')
    #print(elem, end='')
    #print(elem, end='!')
