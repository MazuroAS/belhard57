#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

t = float(input('Введите первое число'))
w = float(input('Введите второе число'))
m = float(input('Введите третье число'))
number_plus=0
number_minus=0
if t>=0:
    number_plus+=1
else:
    number_minus+=1
if w>=0:
    number_plus+=1
else:
    number_minus+=1
if m>=0:
    number_plus+=1
else:
    number_minus+=1
print(number_plus)
print(number_minus)