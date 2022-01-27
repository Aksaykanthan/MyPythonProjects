
from base64 import b64encode, b64decode

password = "my_password"
password = password.encode("utf-8")

encode = b64encode(password)
print(encode)

decode = b64decode(encode)
print(decode)
