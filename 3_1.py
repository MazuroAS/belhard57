#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя  способами

# метод 1 просто через  replace
text: str = 'first friday'
print(text.replace(' ','-'))


# метод  просто через  цикл if c условием, что если нет ля замены ничего, нам оператор напечатает это
text_2: str = 'firstfriday'
a=' '
if a in text_2:
        print(text_2.replace(' ','-'))
else:
    print('нет символов для замены')


# вариант, рассмотренный на занятии
text:str = input()result_1str="-".join(text.split(" "))




