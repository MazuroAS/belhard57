# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

# вариант 1
def split(n):
    return [i for i in n]
n = (input('введите любой текст с клавиатуры'))
k = len(n)  # выводит число символов во введенном с клавы тексте
print("кол-во символов, введенных с клавиатуры : ",k)
print("введенный с клавиатуры текст: ", n)
result = dict(zip(list(n),[list(n).count(i) for i in list(n)]))
print("Dictionary :",result)

# вариант 2
text:  str = input('введите текст: ')
counter: dict = {symbol: text.count(symbol) for symbol in text}
print(counter)





