# function which I thought was helpful, if implemented!!!
def change_pixel(coords: tuple, pixel : bytearray) -> bytearray:
    msg = f"PixelPoker ({coords[0]},{coords[1]})".encode()
    arr = [0] * 512

    for i in range(256):
        arr[i + 256] = i
        arr[i] = msg[i % len(msg)]

    v5 = 0
    for i in range(256):
        v5 = (arr[i] + arr[i + 256] + v5) % 256
        arr[v5 + 256], arr[i + 256] = arr[i + 256], arr[v5 + 256]

    v8, v11 = 0, 0
    for i in reversed(range(4)):
        v8 = (v8 + 1) % 256
        v11 = (arr[v8 + 256] + v11) % 256
        arr[v11 + 256], arr[v8 + 256] = arr[v8 + 256], arr[v11 + 256]
        pixel[i] ^= arr[(arr[v8 + 256] + arr[v11 + 256]) % 256 + 256]

    return pixel[1:]

# click the pixel (95, 313) and get the flag!!!

# stored value, b"FLARE-On"
# x cord is upper-bytes mod 0x2e5
# y cord is lower-bytes mod 0x281

# the program fixes the image for us, iteratively in that case!!!
# 0x52414C46 % 0x2e5 = 95
# 0x6E4F2D45 % 0x281 = 313
