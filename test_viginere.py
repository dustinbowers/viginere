import unittest
from viginere import Viginere


class ViginereUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.viginere = Viginere()
        self.key = 'lemon'
        self.plaintext = 'ATTACKATDAWN'
        self.ciphertext = 'LXFOPVEFRNHR'

    def test_encryption(self):
        encrypted = self.viginere.process(self.key, self.plaintext)
        self.assertEqual(encrypted, self.ciphertext)

    def test_decryption(self):
        decrypted = self.viginere.process(self.key, self.ciphertext, decrypt=True)
        self.assertEqual(decrypted, self.plaintext)
