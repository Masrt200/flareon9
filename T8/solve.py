from rsource import encrypt
from base64 import b64decode, b64encode

code = b"ahoy"
secret = "ydN8BXq16RE=" # "VYBUpZdG" 
for rand in range(65536):
    key = f"FO9{rand}".encode()
    if encrypt(key,code) == b64decode(secret):
        break
# 14 Jun 2022 16:14:36 - 637ms
print(f'key -> {key.decode()}')
data = b"TdQdBRa1nxGU06dbB27E7SQ7TJ2+cd7zstLXRQcLbmh2nTvDm1p5IfT/Cu0JxShk6tHQBRWwPlo9zA1dISfslkLgGDs41WK12ibWIflqLE4Yq3OYIEnLNjwVHrjL2U4Lu3ms+HQc4nfMWXPgcOHb4fhokk93/AJd5GTuC5z+4YsmgRh1Z90yinLBKB+fmGUyagT6gon/KHmJdvAOQ8nAnl8K/0XG+8zYQbZRwgY6tHvvpfyn9OXCyuct5/cOi8KWgALvVHQWafrp8qB/JtT+t5zmnezQlp3zPL4sj2CJfcUTK5copbZCyHexVD4jJN+LezJEtrDXP1DJNg=="
data = b64decode(data)

print(encrypt(key, data))