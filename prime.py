num = int(input("Enter any value: "))
if num > 1:
    for i in range(2, number):
        if (numb % i) == 0:
            print(num, "is not a prime number")
            break;
    else:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
