def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_decipher(text, key):
    return caesar_cipher(text, -key)

def after_security():
    print("AS: Operácia prebehla bezpečne.")

if __name__ == "__main__":
    mode = input("Zadaj mód (s = šifrovať, d = dešifrovať): ").strip().lower()
    text = input("Zadaj text: ")
    key = int(input("Zadaj číselný kľúč: "))
    if mode == "s":
        print("Zašifrovaný text:", caesar_cipher(text, key))
        after_security()
    elif mode == "d":
        print("Dešifrovaný text:", caesar_decipher(text, key))
        after_security()
    else:
        print("Neznámy mód.")