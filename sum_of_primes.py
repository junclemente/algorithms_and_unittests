# Find the sum of the primes numbers below or equal to the entered number.


def prime_sum(number):

    if number <= 1:
        return 1
    if number == 2:
        return 2
    list_of_primes = [2]
    next_num = 3
    while next_num <= number:
        prime_test = True
        for primes in list_of_primes:
            if next_num % primes == 0:
                prime_test = False
                break
            if next_num < primes * primes:
                break
        if prime_test:
            list_of_primes.append(next_num)
        next_num += 2
        # print list_of_primes

    return sum(list_of_primes)
