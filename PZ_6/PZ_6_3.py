# Вариант 8.
# 3. Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
# этого элемента и его соседей.
import random  # подключаем библиотеку

N = int(input("введите число N >> "))  # вводим значение N
a = []  # пустой список для случайных чисел
t = 0  # переменная для работы над циклом
while t < N:  # цикл который добовляет случайные значения
    a.append(random.randint(1, 100) ) # добовляет сучайные значения 1 до 100 в список
    t += 1  # плюс один к занченнию работы цикла
print(a)  # выводим готовый список

def arifm(a): # создаём функцию
    list = [] # пустой список для записи среднего арифмитического
    b = -1 # переменная индекса
    c = 1 # переменная индекса
    for i in a: # цикл поиска среднего арифмитического
        if i == a[0]: # если i равно первому элементу в списке
            list.append((a[1] + a[0]) / 2) # добовляем среднее арифмитическое в новый список
        elif i == a[-1]: # если i равно последнему элементу в списке
            list.append((a[-1] + a[-2]) / 2) # добовляем среднее арифмитическое в новый список
        else: # если i не равно первому или последнему элементу
            list.append(( i + a[b] + a[c]) / 3) # добовляем среднее арифмитическое в новый список
        b +=1 # прибовляем к значению индекса 1
        c +=1 # прибовляем к значению индекса 1
    return  list # возращаем значения list
print(arifm(a)) # выводим функцию