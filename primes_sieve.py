# we will use the sieve of Eratosthenes to find all primes below a given number
from math import sqrt

def primes_sieve(limit):
    nums =[True] * (limit + 1)
    nums[0] = nums[1] = False
    for i in range(2 , int(sqrt(limit)) + 1):
        if nums[i]:
            for j in range(i * i , limit + 1 , i):
                nums[j] = False
    return dict(enumerate(nums))

print(primes_sieve(int(input("Enter the number: "))))