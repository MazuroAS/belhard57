# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input('введите n'))
for b in range(n + 1):
    ee = {'name': 0, 'email': 0}
    cc = input('Введите name')
    dd = input('Ведите email')
    ee_2 = {'name': cc, 'email': dd}
    b = b + 1
    ee.update(ee_2)
    print(ee)










