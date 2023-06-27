#!/usr/bin/python3
"""
Prime Game
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Marian or Benson) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Marian = Benson = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Benson += 1
        else:
            Marian += 1
    if Marian > Benson:
        return 'Marian'
    elif Benson > Marian:
        return 'Benson'
    return None
