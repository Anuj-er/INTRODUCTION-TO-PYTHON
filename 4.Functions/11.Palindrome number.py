def checkPalindrome(num):
    n = num
    rn = 0    
    while(n > 0):    
       r = n %10    
       rn = (rn *10) + r    
       n = n //10    
    if rn == num:
        return True
    else:
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')