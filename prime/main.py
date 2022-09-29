import sys
num1 = int(sys.argv[1])
num1 = 7
if num1 >1:
    for i in range(2,int(num1/2)+1):
        if (num1%i)==0:
            print(num1, "not a prime no")
            break
        else:
            print(num1, "prime no")
else:
    print(num1,"not a prime no")












