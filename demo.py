from .encryption import encrypt
from .decryption import decrypt

def demo():
    sample = input('Enter plaintext to encrypt: ')
    print('Plaintext:', sample)

    aa, key = encrypt(sample, start_sig='ATG', end_sig='TAG')
    print('\nCiphertext (AA sequence):', aa)
    print('\nKey (intron count):', len(key['introns']))

    recovered = decrypt(aa, key)
    print('\nRecovered:', recovered)
    print('\nMatch:', recovered == sample)


if __name__ == '__main__':
    demo()