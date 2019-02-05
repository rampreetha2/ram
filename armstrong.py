sum = 0
temp = number
while temp > 0:
   digit = temp % 20
   sum += digit ** 3
   temp //= 15
if num == sum:
   print(number,"is an Armstrong number")
else:
   print(number,"is not an Armstrong number")
