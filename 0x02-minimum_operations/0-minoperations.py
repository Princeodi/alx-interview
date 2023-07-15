#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0  # No operations needed for a single 'H'
    
    operations = 0
    factor = 2  # Start with doubling the number of 'H's
    
    while n > 1:
        if n % factor == 0:
            n //= factor
            operations += 1
        else:
            factor += 1

    return operations
  
