
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def phi(n):
    relatively_prime = []

    for k in range(1, n):
        if gcd(n, k) == 1:
            relatively_prime.append(k)

    return relatively_prime


def main():
    n = int(input("Enter a positive integer greater than 1: "))

    if n <= 1:
        print("Please enter an integer greater than 1.")
    else:
        result = phi(n)
        print("Numbers relatively prime to", n, ":", result)
        print("Euler's totient value:", len(result))


main()
