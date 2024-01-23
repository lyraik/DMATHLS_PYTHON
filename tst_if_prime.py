def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Return the prime factors of a non-prime number."""
    factors = []
    # Divide by 2 while the number is even
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If the number is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

def test_number(n):
    """Test if a number is prime, and if not, return its prime factors."""
    if is_prime(n):
        return f"{n} is a prime number."
    else:
        factors = prime_factors(n)
        return f"{n} is not a prime number. Its prime factors are: {factors}"

# Example usage
number = 1234321
result = test_number(number)
print(result)
print(test_number(1235321))
print(test_number(63973))

