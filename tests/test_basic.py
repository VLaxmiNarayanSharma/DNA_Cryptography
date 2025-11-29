from src.encryption import encrypt
from src.decryption import decrypt




def test_roundtrip():
    text = 'Testing 123'
    aa, key = encrypt(text)
    recovered = decrypt(aa, key)
    assert recovered == text
