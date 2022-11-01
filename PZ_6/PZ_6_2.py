# Вариант 8.
import random # подключаем библиотеку
D=int(input("введите N>> "))
list = [random.randint(0, 20) for a in range(D)]  # создаём список с случайными 10 числами
print(list)  # выводим список
r=0 # создаём переменную
c=0 # создаём переменную
for j in range(len(list)-2): # цикл поиска моннотонности
    if list[j+2] > list[j+1] > list[j]:
        c+=1
    elif c>=1 and list[j+1] > list[j+2]:
        r+=1
        c=0
if list[-1] > list[-2] > list[-3]:# ищет моннотоность в последнис числах списка
    r+=1
print(r)#выволит результат