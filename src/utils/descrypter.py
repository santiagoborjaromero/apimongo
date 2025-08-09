import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt(data):
    passphrase = "7PToGGTJ71knRd86WF39wfj619qewnbZ"
    key = passphrase.encode('utf-8')[:32]
    iv = b'cAbBrz3Lzy4Ucwhx'

    try:
        cdata1 = base64.b64decode(data)
        cdata = base64.b64decode(cdata1)
        ciphertext = cdata

        # assert iv == iv_received, f"El IV no coincide {iv} {iv_received}"

        if len(ciphertext) % AES.block_size != 0:
            raise ValueError("El texto cifrado no tiene tamaño múltiplo de 16 bytes")

        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        plaintext_padded = cipher.decrypt(ciphertext)

        try:
            plaintext = unpad(plaintext_padded, AES.block_size).decode('utf-8')
        except (ValueError, TypeError):
            plaintext = plaintext_padded.decode('utf-8', errors='replace').rstrip('\x00').strip()

    except Exception as e:
        plaintext = f"Error al descifrar: {str(e)}"

    return plaintext