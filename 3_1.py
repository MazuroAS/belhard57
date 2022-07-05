#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя  способами

# метод 1 просто через  replace
text: str = 'first friday'
print(text.replace(' ','-'))


# вариант 2, рассмотренный на занятии
text_2: str = 'last day'
result_2: str = "-".join(text_2.split(" "))
print(result_2)

#вариант 3  поочередно через split и join
text_3: str = 'good evening'
result_3: str = text_3.split(' ')
result_4: str = '-'.join(result_3)
print(result_4)






