import ast
from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    with open("fernet_key.key", 'wb') as f:
        f.write(key)

def encrypt(inf):
    with open("fernet_key.key", 'rb') as f:
        key_stored = f.read()
    fernet = Fernet(key_stored)
    info = bytes(inf , "utf-8")
    token = fernet.encrypt(info)
    return str(token)
def decrypt(_token):
    with open("fernet_key.key", 'r') as f:
        key_stored = f.read()
    fernet = Fernet(key_stored)
    _token = ast.literal_eval(_token)
    _info = fernet.decrypt(_token).decode('utf-8')
    return _info 
    
    
    