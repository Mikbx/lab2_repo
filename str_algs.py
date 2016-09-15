arr1 = "hello, world!" #объявляем переменную типа стринг
def re(x):
    i = len(x) #определяем длинну строки
    c = ""
    while i > 0:
        i = i - 1
        c = c + x[i]  #добавляем в новую строку символы с конца старой
    return c

print(re(arr1))