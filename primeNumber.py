def countPrime(lis):
    '''
    Return the number of prime numbers in an int list
    '''
    count = 0
    for y in [y for y in lis]:
        if y == 0:
            continue
        x = y // 2
        while x > 1:
            if y % x == 0:
                break
            x = x - 1
        else:
            count += 1
    return count
