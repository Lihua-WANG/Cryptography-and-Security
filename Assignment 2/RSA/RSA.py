# b^p % n
def exp_mod(b, p, n):
    r = 1
    while n:
        if n & 1:
            r = (r * b) % p
        b = (b * b) % p
        n >>= 1
    return r


"""if x and n are coprime: return  S/x % n
    else: return 0 in this case"""
def divide(S, x, n):
    if x % n == 0:
        return 0, 1, n
    next_x = x
    next_n = n
    q = []
    while next_x % next_n != 0:
        q.append(-1 * (next_x // next_n))
        (next_x, next_n) = (next_n, next_x % next_n)
    (next_x, next_n, gcd) = (1, q.pop(), next_n)
    while q:
        (next_x, next_n) = (next_n, next_n * q.pop() + next_x)
    return (S * next_x) % n


def sign(M, n, d):
    return exp_mod(M, n, d)


# S = sign(M, n. d)
def verify(S, n, e, M):
    verified_signature = exp_mod(S, n, e)
    return verified_signature == M


def blindSign(M, n, d, e, x):
    blind = M * (exp_mod(x, n, e))
    signature_of_blind = sign(blind, n, d)
    unblinded_signature_of_blind = divide(signature_of_blind, x, n)
    return signature_of_blind, unblinded_signature_of_blind


def main():
    # SID: 1164051
    x = 4051
    M = 3141592656405193
    n = 1139631134290681913324518075250462509444792614577115360833700594253534083115108212461164873379591734542309312064780949257819665132832661342154198437454459926525649486600336464897081397167045104842672493488133506984881500857942197501
    e = 65537
    d = 207295768068102279456514335033046425303132165927244033393328116698908705079805377126654354876758366533086185042407386444469697300448993171079415022477995849594447981729168914639729964957529446229650186590220990592254700038562058305
    print("The signature is\n", sign(M, n, d), "\n")
    print("The signature is valid? ", verify(sign(M, n, d), n, e, M), "\n")
    print("The blind signature is\n", blindSign(M, n, d, e, x)[0], "\n")
    print("The unblind signature is\n", blindSign(M, n, d, e, x)[1], "\n")
    print("The unblind signature is equal to signature of original message? ",
          blindSign(M, n, d, e, x)[1] == sign(M, n, d))


if __name__ == '__main__':
    main()
