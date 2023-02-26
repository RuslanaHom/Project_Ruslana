Nomer = int(input('Укажите номер места в плацкартном вагоне'))
if (Nomer > 54):
    print('Такого номера не существует, попробуйте снова')
elif (Nomer > 0 and Nomer < 37):
    print('Ваше место в купе')
elif Nomer %2 == 0 and Nomer <= 36:
    print('Верхнее место в купе')
elif Nomer %2!=0 and Nomer <= 35:
    print('Нижнее место в купе')
elif Nomer %2 == 0 and Nomer > 36:
    print('Верхнее боковое')
else:
    print('Нижнее боковое')
