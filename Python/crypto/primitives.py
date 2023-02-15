""" Encryption and decryption primitives.
ord : gets a number from a character
chr : gets a character from a number
charset : string.ascii_letters + string.digits + string.punctuation + " "
modulus : The size of a number

Step 1: Convert the message to a list of numbers
Step 2: Add the key to each number
Step 3: Convert the numbers back to characters
"""


# Shift/Caesar Cipher
def shift(key, text):
    shifted_txt = ""
    for i in text:
        shifted_txt += chr(ord(i) + key)
    return shifted_txt


cipher_txt = shift(1, "Hello Anon")
print(cipher_txt)
decrypted = shift(-1, cipher_txt)
print(decrypted)
