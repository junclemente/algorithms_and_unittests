import unittest
from sum_of_primes import prime_sum

"""
This algorithm is used to find the sum of all prime numbers that are
less than or equal to the provided number which is always a positive integer.

My solution creates a list dynamically by testing odd numbers to see if they
fit the definition of a prime number. If it passes, then it is added to the
list of determined primes.

The efficiency of this solution is O(n^2).
There is an algorithm named Sieve of Eratosthenes which I haven't looked into
depth yet but should increase the efficiency of this algorithm.
"""


class SumOfPrimesTestCase(unittest.TestCase):

    def test_basic_case_equals(self):
        self.assertEqual(prime_sum(10), 17)

    def test_primes_of_10(self):
        self.assertEqual(prime_sum(5), 10)

    def test_primes_of_50(self):
        self.assertEqual(prime_sum(50), 328)

    def test_primes_of_1000(self):
        self.assertEqual(prime_sum(1000), 76127)

    def test_primes_of_5000(self):
        self.assertEqual(prime_sum(5000), 1548136)

    def test_primes_of_25000(self):
        self.assertEqual(prime_sum(25000), 32405717)


if __name__ == '__main__':
    unittest.main()
