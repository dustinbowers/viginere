#!/usr/local/bin/python

import sys

ord_start = ord('A')
grid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
grid_len = len(grid)

def cipher(key, message, direction=0):
    output = [None] * len(message)
    inphrase_upper = message.upper()
    key_upper = key.upper()

    i = 0
    keylen = len(key)
    for c in inphrase_upper:
        char_i = ord(inphrase_upper[i])
        char_index = char_i - ord_start
        key_char = key_upper[i % keylen]
        key_index = grid.index(key_char)
        if direction == 0:
            grid_offset = (char_index + key_index) % grid_len
        elif direction == 1:
            grid_offset = (char_index - key_index) % grid_len

        code = grid[grid_offset]
        output[i] = code
        i = i+1

    return ''.join(output)

def main():
    # process command line args
    argv = sys.argv
    key = argv[1]
    inphrase = argv[2]

    outphrase = cipher(key, inphrase)
    decoded = cipher(key, outphrase, 1)

    print "key: {0}\ninput: {1}\nciphertext: {2}\ndecoded : {3}".format(key, inphrase, outphrase, decoded)

if __name__ == "__main__":
    main()

