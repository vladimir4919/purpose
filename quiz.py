#d={'Адриано Челентано':"1938",'Элвис Прэсли':'1935', 'Владимир Высоцкий':'1938',"Юрий Антонов":'1945',"Стрейзенд":'1942'
   # ,"Миноуг": '1968', "Зыкина": "1929", "Маккартни":'1942','Амстронг': "1900",'Джексон': '1958' }
import random

year_true=0
year_false=0
while 1!=2:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    result = random.sample(numbers, 5)
    for elem in result:
        if elem==1:
            born_Челентано = str(input("дата рождения Челентано?ответ:dd.mm.yyyy="))
            if born_Челентано =='06.01.1938' :
                year_true += 1
            else:
                year_false += 1
                print('Адриано Челентано: шестое января 1938 года')
        elif elem==2:
            born_Прэсли = str(input("дата рождения Прэсли?ответ:dd.mm.yyyy="))
            if born_Прэсли == '08.01.1938':
                year_true += 1
            else:
                year_false += 1
                print('Прэсли: восьмое января 1938 года')
        elif elem==3:
            born_высоцкий = str(input("дата рождения высоцкий?ответ:dd.mm.yyyy="))
            if born_высоцкий == '25.01.1938':
                year_true += 1
            else:
                year_false += 1
                print('высоцкий: двадцать пятое января 1938 года')
        if elem == 4:
            born_Антонов = str(input("дата рождения Антонов?ответ:dd.mm.yyyy="))
            if born_Антонов == '19.02.1945':
                year_true += 1
            else:
                year_false += 1
                print('Антонов: девятнадцатое февраля  1945 года')
        elif elem == 5:
            born_стрейзенд = str(input("дата рождения стрейзенд?ответ:dd.mm.yyyy="))
            if born_стрейзенд == '24.04.1942':
                year_true += 1
            else:
                year_false += 1
                print('Стрэйзенд: двадцать четвертое апреля 1942 года')

        elif elem == 6:
            born_миноуг = str(input("дата рождения миноуг?ответ:dd.mm.yyyy="))
            if born_миноуг == '28.05.1968':
                year_true += 1
            else:
                year_false += 1
                print('Миноуг: двадцать восьмое мая 1968 года')
        elif elem == 7:
            born_Зыкина= str(input("дата рождения Зыкина?ответ:dd.mm.yyyy="))
            if born_Зыкина == '10.06.1929':
                year_true += 1
            else:
                year_false += 1
                print('Зыкина: десятое июня 1929 года')
        elif elem == 8:
            born_маккартни = str(input("дата рождения маккартни?ответ:dd.mm.yyyy="))
            if born_маккартни == '18.06.1942':
                year_true += 1
            else:
                year_false += 1
                print('маккартни: восемнадцатое июня 1942 года')
        elif elem == 9:
            born_армстронг = str(input("дата рождения армстронг?ответ:dd.mm.yyyy="))
            if born_армстронг == '04.07.1900':
                year_true += 1
            else:
                year_false += 1
                print('армстронг: четвертое  июля 1900 года')
        elif elem == 10:
            born_джексон = str(input("дата рождения джексона?ответ:dd.mm.yyyy="))
            if born_джексон == '29.08.1958':
                year_true += 1
            else:
                year_false += 1
                print('джексон: двадцать девятое августа 1958 года')

    procent_true=float((year_true*100)/5)
    procent_false=float((year_false*100)/5)
    print("procent_true:", procent_true)
    print("procent_false:", procent_false)
