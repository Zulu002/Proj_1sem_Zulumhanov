# Вариант 8.
# 3. Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
# этого элемента и его соседей.
import random
N = int(input("введите число N >> "))
a=[]
t=0
c = 0
while  t<N:
    a.append(random.randint(1,10))
    t+=1
print(a)
index1=a[0]
index2=a[1]
index3=a[2]
for i in range(2,N-1):
    a[i-1]=(index1 + index2 + index3) / 3
    index1, index2, index3=index2, index3, a[i+1]
a[i]=(index1 + index2 + index3) / 3
print(a)