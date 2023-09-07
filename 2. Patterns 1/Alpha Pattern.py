n = int(input())
i = 1

while i <= n:
    j = 1
  
    while j <= i:
        print("", end="")
        j += 1
 
    j = 1
    while j <= i:
        print(chr(64 + i), end="")
        j += 1
    
    print()
    i += 1
