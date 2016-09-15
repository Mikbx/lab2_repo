arr1 = [1,2,3,4,5,6,7,8,9,10,11,12,12,11,10,9,8,7,6,5,4,3,2,1]

def min(x): #минимум
    a = x[0]
    i=0
    while i < len(x)-1:
        i=i+1
        if a > x[i]:
            a = x[i]
    return a

def avr(x):  #среднее значение
    i=0
    sum=0
    while i < len(x)-1:
        i=i+1
        sum = sum + x[i]
    av = sum/len(x)
    return av

print(min(arr1))

print(avr(arr1))