import math

def encryptMessage(msg, key):
    print("Original Message:", msg)
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))

    # Add padding if necessary
    fill_null = int((row * col) - msg_len)
    if fill_null > 0:
        msg_lst.extend('_' * fill_null)
    print("Message with Padding:", ''.join(msg_lst))

    # Create the matrix
    matrix = [msg_lst[i:i + col] for i in range(0, len(msg_lst), col)]
    print("Matrix:")
    for r in matrix:
        print(r)

    # Generate ciphertext using the key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
    print("Ciphertext:", cipher)
    return cipher


def decryptMessage(cipher, key):

    print("Ciphertext:", cipher)

    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    col = len(key)
    row = int(math.ceil(msg_len / col))

    key_lst = sorted(list(enumerate(key)), key=lambda x: x[1])

    dec_cipher = [[None for _ in range(col)] for _ in range(row)]

    for _ in range(col):
        curr_idx = key_lst[k_indx][0]

        for j in range(row):
            if msg_indx < msg_len:
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1

        k_indx += 1

    print("Decryption Matrix:")
    for r in dec_cipher:
        print(r)

    try:
        msg = ''.join([''.join(filter(None, row)) for row in dec_cipher])
    except TypeError:
        raise TypeError("Decryption failed: Invalid ciphertext or key.")

    # remove padding
    null_count = msg.count('_')
    if null_count > 0:
        msg = msg[:-null_count]

    print("Decrypted Message:", msg)

    return msg