n = input()
count = 0
sum_even = 0
sum_odd = 0

while count < len(n): 
    if int(n[count]) % 2 == 0:
        sum_even =sum_even+ int(n[count])
    else:
        sum_odd = sum_odd + int(n[count]) 
    count =count+ 1

print(sum_even," ",sum_odd)