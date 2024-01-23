def is_divisible_by_fermat(base, exponent, divisor):
    """
    Checks if 'divisor' is a divisor of 'base^exponent + 1' using Fermat's Little Theorem.
    Assumes 'divisor' is a prime number.
    """
    # Fermat's Little Theorem: a^(p-1) ≡ 1 (mod p) for prime p and a not multiple of p
    # So, we need to check if base^(divisor-1) ≡ 1 (mod divisor), then use it to simplify base^exponent
    if pow(base, divisor - 1, divisor) != 1:
        return False  # Not following Fermat's theorem

    # Simplify base^exponent modulo divisor
    simplified_exponent = exponent % (divisor - 1)
    result = pow(base, simplified_exponent, divisor)

    # Check if result + 1 is divisible by divisor
    return (result + 1) % divisor == 0

# Checking if 17 is a divisor of     11 ^104   + 1
is_divisible = is_divisible_by_fermat(11, 104, 17)
is_divisible
