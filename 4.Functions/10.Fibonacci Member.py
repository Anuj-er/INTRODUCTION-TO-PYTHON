def checkMember(n):
    a1 =0
    a2 =1
    while a1<n:
        a3=a1+a2
        a1=a2
        a2=a3
    if a1==n:
        return True
    else:
        return False
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
