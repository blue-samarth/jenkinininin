# we will use the sieve of Eratosthenes to find all primes below a given number
from math import sqrt
import sys

def primes_sieve(limit):
    nums =[True] * (limit + 1)
    nums[0] = nums[1] = False
    for i in range(2 , int(sqrt(limit)) + 1):
        if nums[i]:
            for j in range(i * i , limit + 1 , i):
                nums[j] = False
    return dict(enumerate(nums))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        # primes_sieve(number)
        primes = [key for key, value in primes_sieve(number).items() if value]
        count = len(primes)
        print(primes , count)
    else:
        print("Please provide a number as a command-line argument.")