from os import getenv
from dotenv import load_dotenv
import base64

load_dotenv()

CRYPTO_KEY = getenv('CRYPTO_KEY')

def encode_variable_name(variable_name: str, team_access_id: str) -> str:
    variable = (variable_name + "/" + team_access_id).encode('utf-8')
    encrypted_bytes = bytearray()
    for i in range(len(variable)):
        key_c = CRYPTO_KEY[i % len(CRYPTO_KEY)].encode('utf-8')
        encrypted_c = variable[i] ^ key_c[0]
        encrypted_bytes.append(encrypted_c)
    encrypted_data = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_data

def decode_variable_name(encoded_data: str) -> str:
    encrypted_bytes = base64.b64decode(encoded_data)
    decrypted_chars = []
    for i in range(len(encrypted_bytes)):
        key_c = CRYPTO_KEY[i % len(CRYPTO_KEY)].encode('utf-8')
        decrypted_c = encrypted_bytes[i] ^ key_c[0]
        decrypted_chars.append(chr(decrypted_c))
    decrypted_data = ''.join(decrypted_chars).encode('latin-1').decode('utf-8')
    return decrypted_data.split('/')[0]