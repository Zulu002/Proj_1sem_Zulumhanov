# Вариант 8
# 1. Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из
# символов C.
a = int(input("Введите число N >> "))  # вводим значение N
b = input("Введите символ >> ")  # вводим символ
c = ""  # создаём переменную для добавления символов
d = 0  # переменная для работы цикла
if a > 0:  # проверяем положительное ли значение
    if len(b) == 1:
        while d < a:  # цикл который добовляет символы
            c = c + b  # добовляет заданный символ
            d += 1  # плюс один к занченнию работы цикла
    else: # если нет
        print("error") # выводим ошибку
print(c)  # выводим готовый список
