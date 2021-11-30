import numpy as np
import textwrap

from extended_euclid import inverse

m = 5
p_dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
         'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
         'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
         'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
         'Z': 25, '0': 26, '1': 27, '2': 28, '3': 29, '4': 30,
         '5': 31, '6': 32, '7': 33, '8': 34, '9': 35, ' ': 36}

c_dic = {c: p for p, c in p_dic.items()}


def convert_to_matrix(texts):
    matrix = []
    for text in texts:
        row = np.array([p_dic[p] for p in text])
        matrix.append(row)
    return np.array(matrix)


def sub_determinant(matrix, i, j, mod=37):
    tmp = np.delete(matrix, j, 0)
    sm = np.delete(tmp, i, 1)
    return int(round(np.linalg.det(sm))) % mod


def decrypt(ciphertext, key):
    c = np.array([p_dic[c] for c in ciphertext])
    p = np.dot(c, key) % 37
    return ''.join([c_dic[n] for n in p])


def main():
    plaintexts = ['X9B6T', '6JAW3', 'UEY7F', 'HIW64', '0515Z']
    ciphertexts = ['2Q59Z', 'Z1Z64', '051UM', 'DNY2J', 'HINTS']

    matrix_P = convert_to_matrix(plaintexts)
    matrix_C = convert_to_matrix(ciphertexts)

    print("Matrix P =\n", matrix_P)
    print("Matrix C =\n", matrix_C)

    # Calculate the determinant of matrix P
    det_P = int(round(np.linalg.det(matrix_P))) % 37
    print("Determinant of P =", det_P)

    # Calculate the inverse of the determinant of matrix P
    inv_m = inverse(det_P, 37) % 37
    print("(det P)^-1 mod 37 =", inv_m)

    # calculate inverse of each item in matrix P
    inv_P = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            inv_P[i].append(inv_m * (-1) ** (i + j) * sub_determinant(matrix_P, i, j))

    inv_P = np.array(inv_P) % 37
    print("P^-1 = \n", inv_P)

    # Key is equal to (inverse matrix P * matrix_C)% 37
    K = np.dot(inv_P, matrix_C) % 37
    print("K = \n", K)

    """
    To decrypt the ciphertext, 
    we need to get decryption of key, that is
    calculate the inverse matrix of K.
    """

    # Calculate the determinant of matrix K
    det_K = int(round(np.linalg.det(K))) % 37
    print("Determinant of K =", det_K)

    # Calculate the inverse of the determinant of matrix K
    inv_m = inverse(det_K, 37) % 37
    print("(det K)^-1 mod 37 =", inv_m)

    # calculate the inverse value of each item in matrix K
    inv_K = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            inv_K[i].append(inv_m * (-1) ** (i + j)
                            * sub_determinant(K, i, j))

    inv_K = np.array(inv_K) % 37
    print("K^-1 = \n", inv_K)

    """
    Decrypt cipher text
    """
    test_ciphertext = \
        "A8VS3XRDEON6JEVXGJID13C07L4C1R4Q965XWRA5DQGYWTNHYO4ND8Z"
    test_plaintext = ""
    for c in textwrap.wrap(test_ciphertext, m):
        test_plaintext += decrypt(c, inv_K)

    print("The Plaintext is:\n", test_plaintext)


main()
