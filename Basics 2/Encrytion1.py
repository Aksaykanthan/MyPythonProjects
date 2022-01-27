
from cryptography.fernet import Fernet as f

password = "asdfsdf"

key = f.generate_key()

fernet = f(key)

encpassword = fernet.encrypt(password.encode())

print(f"original string  : {password}")
print(f"encrypted string : {encpassword}")


decpassword = fernet.decrypt(encpassword).decode()

print(f"decrypted string : {decpassword}")
