# Вариант 8.
# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. в каких магазинах нельзя приобрести сыр.
# 2. в каких магазинах можно приобрести одновременно молоко и сахар.
# 3. в каких магазинах можно приобрести соль.

magnit = {"молоко","соль","сахар"} # словарь продуктов магазина магнит
patyorochka = {"мясо","молоко","сыр"} # словарь продуктов магазина пятёрочка
perekrostok = {"молоко","творог","сыр","сахар"} # словарь продуктов магазина перекрёсток
print(1) # первая задача
cheese = "сыр" # пременная в которой лежит значение сыр
if cheese not in magnit: # сравниваем нет ли значения сыр в множестве
    print("В магазине magnit отсутствует сыр") # выводим
elif cheese not in patyorochka: # сравниваем нет ли значения сыр в множестве
    print("В магазине patyorochka отсутствует сыр") # выводим
elif cheese not in perekrostok: # сравниваем нет ли значения сыр в множестве
    print("В магазине perekrostok отсутствует сыр") # выводим
else: # если условие не выполнилось
    print("Везде есть сыр.Ура мы сыты!")


print(2) # вторая задача
s = "сахар" # пременная в которой лежит значение сахар
m = "молоко" # пременная в которой лежит значение молоко
if s in magnit and m in magnit: # сравниваем есть ли значение сахар и молоко в множестве
    print("В магазине magnit есть молоко и сахар") # выводим
if s in patyorochka and m in patyorochka: # сравниваем есть ли значение сахар и молоко в множестве
    print("В магазине patyorochka есть молоко и сахар") # выводим
if s in perekrostok and m in perekrostok: # сравниваем есть ли значение сахар и молоко в множестве
    print("В магазине perekrostok есть молоко и сахар") # выводим
else: # если условие не выполнилось
    print("нету ни сахара ни молока")


print(3) # третья задача
salt = "соль" # пременная в которой лежит значение соль
if salt in magnit: # сравниваем есть ли значение соль в множестве
    print("В магазине magnit есть соль") # выводим
elif salt in patyorochka: # сравниваем есть ли значение соль в множестве
    print("В магазине patyorochka есть соль") # выводим
elif salt in perekrostok: # сравниваем есть ли значение соль в множестве
    print("В магазине perekrostok есть соль") # выводим
else: # если условие не выполнилось
    print("соли нет")
