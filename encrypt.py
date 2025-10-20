import sys
def letters_only(text):
    """Return True if text has only alphabetic characters."""
    return text.isalpha()

def vigenere_encrypt(data, key):
    """Encrypt text using Vigenère cipher."""
    out, k = [], 0
    for c in data:
        if c.isalpha():
            p = ord(c) - 65
            shift = ord(key[k % len(key)]) - 65
            out.append(chr((p + shift) % 26 + 65))
            k += 1
        else:
            out.append(c)
    return "".join(out)


def vigenere_decrypt(data, key):
    """Decrypt text using Vigenère cipher."""
    out, k = [], 0
    for c in data:
        if c.isalpha():
            p = ord(c) - 65
            shift = ord(key[k % len(key)]) - 65
            out.append(chr((p - shift) % 26 + 65))
            k += 1
        else:
            out.append(c)
    return "".join(out)
