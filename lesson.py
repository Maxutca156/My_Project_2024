def dollars(rub):
    return  rub/91

def euros(rub):
    return rub/100

def pounds(rub):
    return rub/115

def money_changing():
    print('Добро пожаловать в обменный пункт, какую валюту вы хотите купить?')
    print('Если хотите выйти нажмите (выйти).')
    print('Если  хотите узнать курс введите (Доллары/Евро/Фунты  стерлингов).')
    print('1. Доллары\n2. Евро\n3. Фунты стерлингов')
    print('Покажите  ваш паспорт.')
    print('(Показать) или (Не показывать)?')
    while True:
        a = input('Выбирайте: ').lower()
        if a == 'показать':
            print('Хорошо')
        elif a == 'не показывать':
            print('Тогда убирайтесь прочь!')
            break
        else:
            print('Что?')
    while True:
        choice = input('Выберите валюту(1/2/3): ').lower()
        if choice ==  '1':
            money = int(input('Введите вашу сумму в рублях: '))
            print('Вы получите долларов:' ,dollars(money))
        elif choice == '2':
            money = int(input('Введите вашу сумму в рублях: '))
            print('Вы получите евро:' ,euros(money))
        elif  choice == '3':
            money = int(input('Введите вашу сумму в рублях: '))
            print('Вы получите Фунтов стерлингов:' ,pounds(money))
        elif choice == 'выйти':
            print('Возвращайтесь ещё!')
            break
        else:
            print('Не  пишите бред!')
        if  choice == 'доллары':
            print('В 1  долларе 74 рубля.')
        elif  choice == 'евро':
            print('В 1  евро 87 рублей.')
        elif  choice == 'фунты  стерлингов':
            print('В 1  фунте 101 рублей.')