import json
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

data = "MTIzNDU2Nzg5MGFiY2RlZoK5i/TuoYLKIG/j0yE/3xQ0jjUKoGG3mJYcoQnSvKQA"
passphrase = "7PToGGTJ71knRd86WF39wfj619qewnbZ"
key = passphrase.encode('utf-8')[:32]
iv = b'1234567890abcdef'

try:
    cdata = base64.b64decode(data)
    iv_received = cdata[:16]
    ciphertext = cdata[16:]

    assert iv == iv_received, "El IV no coincide"

    if len(ciphertext) % AES.block_size != 0:
        raise ValueError("El texto cifrado no tiene tamaño múltiplo de 16 bytes")

    cipher = AES.new(key, AES.MODE_CBC, iv=iv_received)
    plaintext_padded = cipher.decrypt(ciphertext)

    try:
        plaintext = unpad(plaintext_padded, AES.block_size).decode('utf-8')
    except (ValueError, TypeError):
        plaintext = plaintext_padded.decode('utf-8', errors='replace').rstrip('\x00').strip()

    print(plaintext)
except Exception as e:
    print(f"Error al descifrar: {str(e)}")