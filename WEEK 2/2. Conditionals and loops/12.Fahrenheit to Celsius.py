a = int(input())
b = int(input())
c = int(input())
count = a
while count<=b:
     # f = (celcius*9/5)+32
    f = int((a-32)*5/9)
    print( a,f)
    count = count+c
    a = a +c