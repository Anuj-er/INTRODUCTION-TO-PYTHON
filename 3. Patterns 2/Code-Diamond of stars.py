n = int(input())
firstHalf = (n + 1) // 2
secondHalf = n // 2
# First Half
i = 1 
while i <= firstHalf:
    spaces = 1 
    while spaces <= (firstHalf - i) :
        print(" ", end = "")
        spaces += 1
    j = 1
    while j <= (2 * i) - 1 :
        print("*", end = "")
        j += 1
        
    print()
    i += 1
# Second Half 
i = secondHalf 
while i >= 1 :
    spaces = 1
    while spaces <= (secondHalf - i + 1) :
        print(" ", end = "") 
        spaces += 1
    j = 1 
    while j <= (2 * i) - 1 :
        print("*", end = "") 
        j += 1
    
    print()
    i -= 1
