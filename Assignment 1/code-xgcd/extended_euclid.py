def extended_gcd(a, b):
    prev_x = 0
    prev_y = 1
    x = 1
    y = 0

    while a != 0:
        quotient = b // a
        b, a = a, b % a
        x, prev_x = prev_x - quotient * x, x
        y, prev_y = prev_y - quotient * y, y

    gcd = b
    return gcd, prev_x, prev_y


def inverse(a, n):
    # a and n are 2 positive integers.
    if a <= 0 or n <= 0:
        print("Please input 2 positive integers!")
        return

    # Recall the extended_gcd API.
    gcd, x, y = extended_gcd(a, n)

    # Check if the inverse exists.
    if gcd != 1:
        print(a, 'mod', n, 'does not have an inverse!')
        return

    # Double check the result to be positive.
    if x < 0:
        x += n

    return x


def main():
    a = 545
    b = 99
    gcd, x, y = extended_gcd(a, b)
    print('GCD =', gcd,
          ',\n x =', x,
          ',\n y =', y)

    print('The inverse is:', inverse(a, b))


if __name__ == '__main__':
    main()
