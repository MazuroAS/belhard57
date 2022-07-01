# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами
name='Nastya'
age='29'
city='Minsk'

#конкатенация
all_inf_0 = name + age + city
print(all_inf_0)

# c помощью %
all_inf_1 = "Меня зовут %(n)s.Мне %(a)s лет. Я из города %(c)s.  % {"n": name, "a": age, "c": city}
print(all_inf_1)

#метод format()
all_inf_2='Меня зовут {n}, Мне {a} лет. Я из города {c}.'.format(n=name,a=age,c=city)
print(all_inf_2)
