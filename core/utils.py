import nacl.secret#secretbox to use for encryption and decryption

def get_box():
    with open("secret.key", "rb") as f:#rb for binary
        key = f.read()
    return nacl.secret.SecretBox(key)

def encryptMsg(message: str) -> bytes:#encrypted into bytes
    box = get_box()
    return box.encrypt(message.encode())

def decryptMsg(encrypted: bytes) -> str:#decrypts from bvtes lol
    box = get_box()
    return box.decrypt(encrypted).decode()
