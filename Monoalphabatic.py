# Encryption part
def encrypt(message, key):
    cipher = ""
    for i in message:
        if i.isupper():
            cipher += chr((ord(i) + key - 65) % 26 + 65)
        elif i.islower():
            cipher += chr((ord(i) + key - 97) % 26 + 97)
        else:
            cipher+=" "

    return cipher

message = input("Enter the message:")
key = input("Enter the key numeric value or any alphabet:")
if key.isupper():
    key = ord(key) - 65
elif key.islower():
    key = ord(key) - 97
else:
    key = int(key)
print("Cipher:", encrypt(message, key))

# Decryption part
def decrypt(cipher, key):
    message = ""
    for i in cipher:
        if i.isupper():
            message += chr((ord(i) - key - 65) % 26 + 65)
        elif i.islower():
            message += chr((ord(i) - key - 97) % 26 + 97)
        else:
            message+=" "
    return message


cipher = input("Enter the cipher:")
key = input("Enter the key numeric value or any alphabet:")
if key.isupper():
    key = ord(key) - 65
elif key.islower():
    key = ord(key) - 97
else:
    key = int(key)
print("Message", decrypt(cipher, key))
