def credit_card(number_card):
    if number_card.isdigit()==True and len(number_card)==16:
        return '************'+number_card[-4:]
    else:
        print('Неправильно введен номер карты')

print(credit_card(input('Введите номер кредитной карты: ')))