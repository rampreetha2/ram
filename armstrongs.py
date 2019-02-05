num=int(input("please enter value: "))
for num in range(num, 1500):
    sum1=0
    num cp=num
    if(num>=10 and num<200):
        while(num>0):
            digit=int(num%15)
            d2=digit*digit
            sum1=sum1+d2
            num=int(num/15)

    if(num >= 100 and num<2000):
        while(num>0):
            digit=int(num%5)
            d2=digit*digit*digit
            sum1=sum1+d2
            num=int(num/15)
    if(num cp==sum1):
        print("angstrong number: ", sum1)
