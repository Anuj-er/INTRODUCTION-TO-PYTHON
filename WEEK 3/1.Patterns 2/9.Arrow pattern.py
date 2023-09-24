n = int(input())
m = n // 2 + 1
row = 1

while row <= m:
    spaces = 1
    while spaces < row:
        print(" ", end="")
        spaces += 1
        
    stars = row
    count = 1
    while stars >= row and count <= row:
        print("* ", end="")
        stars += 2
        count += 1
        
    print()
    row += 1
   
row = m - 1   
while row >= 1: 
    spaces = 1
    while spaces < row:
        print(" ", end="")
        spaces += 1
            
    stars = row
    count = 1
    while stars >= 1 and count <= row:
        print("* ", end="")
        stars += 2
        count += 1
        
    print()
    row -= 1
