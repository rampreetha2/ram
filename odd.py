def sumofoddints (n):

   n >= 1

    total = 0

    for number in range (1, n):

        if number % 2 == 1:

            total += n

    return total
