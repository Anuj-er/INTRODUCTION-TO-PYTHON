def Checkarmstrong(n):
    s = str(n)
    numb = n
    answer = 0

    while n>0:
        a = n%10
        answer = answer + a**len(s)
        n = n//10
    if answer == numb:
        print("true")
    else:
        print("false")
n = int(input())
Checkarmstrong(n)