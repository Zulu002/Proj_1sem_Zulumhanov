# Вариант 8
# 1. Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из
# символов C.
a=int(input("Введите число N >> ")) # вводим значение N
b=input("Введите символ >> ") # вводим символ
c=[] # создаём пустой цикл
d=0 # переменная для работы цикла
if a>0: # проверяем положительное ли значение
    while d < a:  # цикл который добовляет символы
        c.append(b)  # добовляет заданный символ
        d += 1  # плюс один к занченнию работы цикла
print(c)  # выводим готовый список