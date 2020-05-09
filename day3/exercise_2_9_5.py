import sympy

top_value = 50
primes_list = list(sympy.sieve.primerange(0, (top_value ** 2) + 1))

try:
    integer=int(input("Please enter an integer less than 50:"))
except ValueError:
    print("Entered number is not integer")
try:
    primes_list.remove(integer)
except Exception:
    None

is_prime = "%d is prime"
for prime in primes_list:
    if prime >= integer and (prime % integer == 0):
        is_prime = "%d is not prime"
        break
    elif prime <= integer and (integer % prime == 0):
        is_prime = "%d is not prime"
        break

print(is_prime % integer)