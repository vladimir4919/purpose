N=int(input('ввести число элементов будущего списка'))
a_number_input=0
spisok=[]
while a_number_input <= N:
    digit=int(input())
    spisok.append(digit)
    a_number_input+=1
print(spisok)
for i in range(len(spisok)-1):
    b=0
    if spisok[i] > spisok[i+1]:
        b=spisok[i+1]
        spisok[i + 1] = spisok[i]
        spisok[i] = b
        print(spisok[0])
    else:
        i+=1
print(spisok)