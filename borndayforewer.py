
def bornyeardayforewer(year_birth,notability,day,month):
    print(year_birth)
    year = int(input(f'Введите год рождения {notability}:'))
    while int(year) != year_birth:
        print("Не верно")
        year = input(f'Введите год рождения {notability}:')
    day = input(f'В какой день {month} день  рождения {notability}:')
    while day != '6':
        print("Не верно")
        day = input(f'В какой день {month} родился {notability}?')
    print('Верно')
notability='Пушкин'
year_birth=1799
day_birth=6
month='июня'
bornyeardayforewer(year_birth,notability,day_birth,month)

notability='Дарвин'
year_birth=1809
day_birth=12
month='февраля'
bornyeardayforewer(year_birth,notability,day_birth,month)