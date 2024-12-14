#!/usr/bin/python3
"""
Module to determine the winner of the prime game.
"""

def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    
    Args:
        x (int): The number of rounds.
        nums (list): An array of n values for each round.
    
    Returns:
        str: The name of the player that won the most rounds. 
             If the winner cannot be determined, returns None.
    """
    
    def sieve(n):
        """Generates a list of prime numbers up to n using the Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [i for i, prime in enumerate(is_prime) if prime]
    
    def playGame(n):
        """Simulates the game for a given n and returns the winner."""
        primes = sieve(n)
        turn = 0  # 0 for Maria, 1 for Ben
        nums_set = set(range(1, n + 1))
        while True:
            move_made = False
            for prime in primes:
                if prime in nums_set:
                    nums_set -= set(range(prime, n + 1, prime))
                    move_made = True
                    break
            if not move_made:
                return "Maria" if turn == 1 else "Ben"
            turn = 1 - turn
    
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = playGame(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    import sys
    x = int(sys.argv[1])
    nums = list(map(int, sys.argv[2:]))
    print(isWinner(x, nums))

