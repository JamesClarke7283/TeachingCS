""" Encryption and decryption primitives.
ord : gets a number from a character
chr : gets a character from a number
charset : string.ascii_letters + string.digits + string.punctuation + " "
modulus : The size of a number

Step 1: Convert the message to a list of numbers
Step 2: Add the key to each number
Step 3: Convert the numbers back to characters
"""

message = "Hello Anon"
key = 1
msg_ord = []
cipher_txt = ""


def encrypt(key, msg):
    cipher_txt = ""
    for i in msg:
        cipher_txt += chr(ord(i) + key)
    return cipher_txt


def decrypt(key, msg):
    cipher_txt = ""
    for i in msg:
        cipher_txt += chr(ord(i) - key)
    return cipher_txt


cipher_txt = encrypt(1, "Hello Anon")
print(cipher_txt)
decrypted = decrypt(1, cipher_txt)
print(decrypted)
