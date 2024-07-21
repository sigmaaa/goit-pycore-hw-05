"""
Fibonacci Module

This module provides a function to generate a memoized Fibonacci function.

The memoized Fibonacci function computes the nth Fibonacci number efficiently
using memoization to cache previously computed results, avoiding redundant calculations.
"""
def caching_fibonacci():
    """
    Returns a memoized Fibonacci function.
    
    The returned function computes the nth Fibonacci number efficiently using memoization
    to cache previously computed results, avoiding redundant calculations.
    
    Example usage:
        fib = caching_fibonacci()
        print(fib(10))  # Output: 55
        
    Returns:
        function: A function that computes the nth Fibonacci number.
    """
    cache = {0:0, 1:1}  # Dict to store computed Fibonacci numbers. Def values: F(0) = 0, F(1) = 1

    def fibonacci(n):
        """
        Computes the nth Fibonacci number using memoization.
        
        Args:
            n (int): The position in the Fibonacci sequence to compute.
        
        Returns:
            int: The nth Fibonacci number.
        """
        if n < 0:
            raise ValueError("Fibonacci number is not defined for negative integers")
        if n in cache:
            return cache[n]  # Return cached value if available
        # Recursive case: Compute F(n) = F(n-1) + F(n-2) and cache the result
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
