# Найти 2 5-ти значных делителя
# числа 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
N = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
# делители находятся в диапазоне от 10 000 до 99 999
for d in range (10000, 99999):
    if N % d == 0 :
        print (d, ' ', sep = '', end = '')
else:
    print('нет в этом диапазоне делителей')

# вариант решения через функцию
def divisors_for_num(our_num):
    result = []
    for i in range(10000, 999999):
        if our_num % i == 0:
            result.append(i)
            result.append(our_num)
    return result
print(divisors_for_num(1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139))


numbers =[1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,4,4,4,5,5,5,5,5,]
i=0
while i<len(numbers):
    for j in range(i+1,len(numbers)-1):
        if numbers[i]==numbers[j]:
            count+=1
        else:
            result.extend([numbers[i],count)
            break
        if numbers[i]==numbers[j]:
            numbers.extend([numbers[i],count)
     i=j
print(result)
                            
                            
  # бинарный поиск
  numbers = [i for i in range(1,100)]
a = 34
i = len(numbers)//2
count =1
while numbers[i] !=a:
    count += 1
    if numbers[i]>a:
        numbers = numbers[:i]
    else:
        numbers = numbers[i+1:]
    i = len(numbers)//2
print(i)
                            
                            

