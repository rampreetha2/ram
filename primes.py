low = int(input("Enter low range: "))
upp = int(input("Enter upp range: "))
 
for number in range(lower,upper + 1):

   if num>1:
       for i in range(2,num):
           if (num % i) == 0:
               break;
       else:
           print(num)
