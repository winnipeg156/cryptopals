import sys
import binascii


def fixed_xor(hex1, hex2):
    bytes1 = binascii.unhexlify(hex1)
    bytes2 = binascii.unhexlify(hex2)
    result = b""
    for i in range(min(len(bytes1), len(bytes2))):
        result += (bytes1[i] ^ bytes2[i]).to_bytes()
    return result


if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    print (fixed_xor(hex1, hex2))
