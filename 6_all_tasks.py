# задача 1
# написать функцию перевода десятичного числа в двоичное и обратно, без использования функции
import lst as lst


def decimal_to_bin_converter(decimal: int) -> str:
# будем делить число на 2 до тех пор, пока больше 1
    result = " "
    while decimal:
        result +=str(decimal % 2)
        decimal //=2
    return result[::-1]
print(decimal_to_bin_converter(15))

# задача 2
# 2 Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе. (словари в помощь)
def text_to_morse(text: str) -> int:
    morse_data = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
             'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '}

    morse: str = ''
    for letters in text.upper():
        if letters in morse_data:
            morse += morse_data[letters] + ' '
    return morse
print(text_to_morse('hello'))


# задача 3
# Дан список чисел и на вход поступает число N, необходимо сместить список на
# # указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def shift(numbers: list, n: int) -> list:
    if abs(n) > len(numbers):
        n -= (n // len(numbers)) * len(numbers)
    if n > 0:
        numbers = numbers[n:] + numbers[:n]
    else:
        numbers = numbers[-n:] + numbers[:-n]
    return
numbers = [1,2,3,4,5,6,7,8,9]
n: int = int(input('ввести число'))
print(shift(numbers, n))

# задача 4
# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка незаконно
def str_sorted(lst: list)-> list:
    return list(filter(lambda x: isinstance(x, str), lst))
print(str_sorted([1,2,3,'sgdf', 'tjgh', True, 5,4, 'gfdh']))

# вариант 2по4 задаче
def str_sorted(lst: list) -> list:
    i = 0
    while i < len(lst):
        if not isinstance(lst[i], str):
            del lst[i]
        else:
            i += 1
    return lst
print(str_sorted([1, 2, 3, 'sgdf', 'tjgh', True, 5, 4, 'gfdh']))

# задача 5
# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
def rev(lst: list) -> lst:
    for i in range(len(lst) // 2):
        lst[i],lst[~i] = lst[~i], lst[i]    # знак ~ домножает на -1
    return lst

# задача 6
# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
def sortedd(numbers: list) ->list:
    i = 0
    while i < len(numbers):
        if not numbers[i] % 2:
            numbers.insert(0,numbers.pop(i))
        else:
            i +=1
    return numbers
print(sortedd([1,2,5,8,10,7]))

# задача 7
# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной стороны списка
def sum_sosedej(numbers: list)->list:
    sosedi = []
    for i in range(len(numbers)):
        if i == len(numbers)-1:
            sosedi.append(numbers[i-1]+numbers[0])
        else:
            sosedi.append(numbers[i-1]+numbers[i+1])
    return sosedi
print(sum_sosedej([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# задача 8
# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
def find_country(city: str) -> str:
    countries = {
    'BY': ['Minsk', 'Btest'],
    'RY' : ['Moscow', 'spb']
    }
    for country, cities in countries.items():
        if city.lower() in cities:
            return country.title()
закончила на 00:44:00