# step 0) read key from file

key = ''
with open('myTopSecret.key', 'rb') as file:
   key = file.read()

# step 1) read data from file

data = ''
with open('file.txt', 'rb') as file:
   data = file.read()

# step 2) encrypt data 
from cryptography.fernet import Fernet

f = Fernet(key)
encryptedData = f.encrypt(data)


# step 3) save the encrypted data into a file

with open('encryptedText1.txt', 'wb' ) as file:
   file.write(encryptedData)






  # step 0) read the key from file 

key = ''
with open('myTopSecret.key', 'rb') as file:
    file.read()

# step 1) read the encrypted data

encryptedData = ''
with open('encryptedText.txt', 'rb') as file:
    file.read()

# step 2) decrypt the data

from cryptography.fernet import Fernet
 
f = Fernet(key)
decryptData = f.decrypt(encryptedData)

print('The Encrypted Text: ', encryptedData.decode())

print('The Decrypted Text: ', decryptData.decode())

