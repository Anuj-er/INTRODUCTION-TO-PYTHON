while True:
    a = int(input())
    if a==1 or a==2 or a==3 or a==4 or a ==5:
            if a ==1:
                b = int(input())
                c = int(input())
                print(b+c)
            elif a ==2:
                b= int(input())
                c = int(input())
                print(b-c)
            elif a ==3:
                b= int(input())
                c = int(input())
                print(b*c)
            elif a ==4:
                b= int(input())
                c = int(input())
                print(int(b/c))
            elif a ==5:
                b= int(input())
                c = int(input())
                print(b%c)
    elif a ==6:
        quit()
    else:
        print("Invalid Operation")
    
