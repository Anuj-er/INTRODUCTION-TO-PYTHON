N = int(input())
if N < 2:
    is_prime = False
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= N:
        if N % divisor == 0:
            is_prime = False
            break
        divisor += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")
