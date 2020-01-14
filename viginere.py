import sys


class Viginere:

    def __init__(self):
        self.grid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.grid_len = len(self.grid)
        self.ord_start = ord(self.grid[0])

    def process(self, key, message, decrypt=False):
        output = [''] * len(message)
        message = message.upper().replace(' ', '')
        key = key.upper()

        i = 0
        keylen = len(key)
        for c in message:
            char_i = ord(message[i])
            char_index = char_i - self.ord_start
            key_char = key[i % keylen]
            key_index = self.grid.index(key_char)
            if decrypt:
                grid_offset = (char_index - key_index) % self.grid_len
            else:
                grid_offset = (char_index + key_index) % self.grid_len

            code = self.grid[grid_offset]
            output[i] = code
            i = i + 1

        return ''.join(output)


def main():
    # process command line args
    if len(sys.argv) != 3:
        print("Usage: python viginere.py <passphrase> <plaintext>")
        return

    argv = sys.argv
    key = argv[1]
    phrase = argv[2]

    viginere = Viginere()
    encrypted = viginere.process(key, phrase)
    decrypted = viginere.process(key, encrypted, decrypt=True)

    print("key: {0}\ninput: {1}\nciphertext: {2}\ndecoded : {3}"
          .format(key, phrase, encrypted, decrypted))


if __name__ == "__main__":
    main()
