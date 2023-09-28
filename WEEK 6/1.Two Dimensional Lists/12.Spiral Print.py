from sys import stdin
#Your code goes here
def spiralPrint(mat, nRows, mCols):
    top = 0
    bottom = nRows - 1
    left = 0
    right = mCols - 1

    while top <= bottom and left <= right:
        # Print the top row
        for i in range(left, right + 1):
            print(mat[top][i], end=" ")

        # Move the top boundary down
        top += 1

        # Print the rightmost column
        for i in range(top, bottom + 1):
            print(mat[i][right], end=" ")

        # Move the right boundary to the left
        right -= 1

        # Check if there are more rows to print
        if top <= bottom:
            # Print the bottom row
            for i in range(right, left - 1, -1):
                print(mat[bottom][i], end=" ")

            # Move the bottom boundary up
            bottom -= 1

        # Check if there are more columns to print
        if left <= right:
            # Print the leftmost column
            for i in range(bottom, top - 1, -1):
                print(mat[i][left], end=" ")

            # Move the left boundary to the right
            left += 1




























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1