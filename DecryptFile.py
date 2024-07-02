# step 0) read the key from file 

key = ''
with open('myTopSecret.key', 'rb') as file:
    key = file.read()

# step 1) read the encrypted data

encryptedData = ''
with open('encryptedText1.txt', 'rb') as file:
   encryptedData = file.read()

# step 2) decrypt the data

from cryptography.fernet import Fernet
 
f = Fernet(key)
decryptData = f.decrypt(encryptedData)

print('The Encrypted Text: ', encryptedData.decode())

print()

print('The Decrypted Text: ', decryptData.decode())
