number_1 = int(input('введите первое целое число:'))
number_2 = int(input('введите второе целое число:'))
number_3 = int(input('введите третье целое число:'))
if number_1==number_2 and number_2==number_3:
    print(3)
elif number_1==number_2 or number_2==number_3 or number_1==number_3:
    print(2)
else: print(0)