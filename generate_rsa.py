def gcd(a, b):
    """Compute the Greatest Common Divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def find_e(phi):
    """Find the minimal e such that gcd(e, phi) is 1."""
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    return e

def mod_inverse(e, phi):
    """Find the modular inverse of e modulo phi."""
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_rsa_key_pair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_e(phi)
    d = mod_inverse(e, phi)

    if d is None:
        raise Exception("Failed to find modular inverse. The chosen primes may not be suitable.")

    return ((n, e), (n, d))

# Given values
p = 7
q = 13


# Generate RSA key pair
public_key, private_key = generate_rsa_key_pair(p, q)
print("RSA Key Pair Generated:")
print("------------------------")
print("public key:  n,  e")
print("Public Key:", public_key)
print("------------------------")
print("private key:  n,  d")
print("Private Key:", private_key)
print("------------------------")
