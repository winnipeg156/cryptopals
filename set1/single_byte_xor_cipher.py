import binascii
from collections import Counter
from fixed_xor import fixed_xor


def score(bytes):
    score = 0
    for byte in bytes:
        if byte in range(65, 123) or byte == 32:
            score +=1
    return score


def crack_xor(cipher_text):
    outputs = []
    scores = []
    for i in range(256):
        key = binascii.hexlify(i.to_bytes() * len(cipher_text))
        output = fixed_xor(cipher_text, key)
        outputs.append(output)

    for output in outputs:
        curr_output = (score(output), output)
        scores.append(curr_output)

    return max(scores) 


if __name__ == "__main__":
    cipher_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(crack_xor(cipher_text)[1])
