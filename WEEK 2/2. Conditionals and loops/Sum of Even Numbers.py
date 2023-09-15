n = int(input())
count = 1
sum = 0
while count<=n:
    if count%2 ==0:
        sum = sum + count
    count = count+1
print(sum)