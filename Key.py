# step 0) go to terminal and write 'pip install cryptography'
# step 1) generate a symmetric key 

from cryptography.fernet import Fernet 
key = Fernet.generate_key()

# step 2) save the key into a file

with open('myTopSecret.key', 'wb') as file:
    file.write(key)