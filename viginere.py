#!/usr/local/bin/python

import sys

key = ''
inphrase = ''
output = ''

ord_start = ord('A')
grid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
grid_len = len(grid)

def process_stdin():
    print(sys.argv)
    argv = sys.argv
    global key, inphrase
    key = argv[1]
    inphrase = argv[2]
    print "keyphrase: {0}\ninput: {1}\nord_start {2}".format(key, inphrase, ord_start)

def cipher(key, message, direction=0):
    output = [None] * len(inphrase)
    inphrase_upper = inphrase.upper()
    key_upper = key.upper()
    print "key_upper {0}".format(key_upper)
    
    if direction == 0:
        print "direction forward\n"
        i = 0
        keylen = len(key)
        print "keylen = {0}".format(keylen)
        for c in inphrase_upper:
            print "===cipher start {0} ====".format(i)
            char_i = ord(inphrase_upper[i])
            char_index = char_i - ord_start
            key_char = key_upper[i % keylen]
            key_index = grid.index(key_char)
            print "char_i {0}\nchar_index {1}\nkey_char {2}\nkey_index {3}".format(char_i, char_index, key_char, key_index)
            grid_offset = (char_index + key_index) % grid_len
            code = grid[grid_offset]
            print "grid offset: {0} - code {1}".format(grid_offset, code)
            output[i] = code
            i = i+1
            print "===cipher end ===\n"
        print output

    else:
        print "direction backward\n"

def main():
    process_stdin()
    print "main key {0}".format(key)
    cipher(key, inphrase)

if __name__ == "__main__":
    main()
