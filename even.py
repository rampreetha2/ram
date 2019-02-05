def sum_even(x, y):
    count = 0
    for i in range(x,y, 1):
        if(i % 2 == 0):
            count += [i]
        return count
