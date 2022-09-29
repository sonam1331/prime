num = 7
if num >1:
    for i in range(2,int(num/2)+1):
        if (num%i)==0:
            print(num, "not a prime no")
            break
        else:
            print(num, "prime no")
else:
    print(num,"not a prime no")












