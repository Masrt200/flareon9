from hashlib import md5

def rc4(key:bytes, pt: bytes) -> bytes:
    s = [*range(0x100)]
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) & 0xff
        s[i], s[j] = s[j], s[i]

    i, j = 0, 0
    ret = []
    for c in pt:
        i = (i + 1) & 0xff
        j = (j + s[i]) & 0xff
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) & 0xff]
        ret.append(k^c)

    return bytes(ret)

# string to wide-string 
# https://stackoverflow.com/questions/402283/stdwstring-vs-stdstring
def str_to_wstr(x):
    y = b""
    for i in x:
        y += bytes([i,0])
    return y

def encrypt(key, data):
    #key = b"FO926712"
    #code = b"ahoy"
    hash = md5(str_to_wstr(key)).hexdigest().encode()
    #hash = hash * 4
    secret = rc4(str_to_wstr(hash), str_to_wstr(data))
    return secret