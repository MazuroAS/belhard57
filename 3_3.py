# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами
name='Nastya'
age='29'
city='Minsk'

#конкатенация
all_inf_0 = name + age + city
print(all_inf_0)

#метод format()
all_inf_2='Меня зовут {n}, Мне {a} лет. Я из города {c}.'.format(n=name,a=age,c=city)
print(all_inf_2)

# c помощью f-string
print(f"Меня зовут, {name}. Мне {age} лет,я из города {city}.")
