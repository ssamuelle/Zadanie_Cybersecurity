from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys():
    # Vygeneruje privátny a verejný kľúč RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Serializácia privátneho kľúča
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Serializácia verejného kľúča
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Uloženie do súborov
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_pem)
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_pem)

    print("Kľúče boli vygenerované a uložené do 'private_key.pem' a 'public_key.pem'.")

if __name__ == "__main__":
    generate_keys()