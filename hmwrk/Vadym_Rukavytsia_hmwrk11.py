""" Julius Caesar's encryption machine"""
from string import ascii_letters


def make_cypher_key(step: int) -> dict:
    """Making cypher key dictionary with step"""
    cypher = {}
    for number, letter in enumerate(ascii_letters, step):
        if number < len(ascii_letters):
            cypher[letter] = ascii_letters[int(number)]
        else:
            cypher[letter] = ascii_letters[int(number)-len(ascii_letters)]
    return cypher


def encrypt_message(text: str, step=3, decrypt=False):
    """Encrypting or decrypting message with step in ascii_letters"""
    cypher = make_cypher_key(step)
    if decrypt:
        cypher = {cypher[k]: k for k in cypher}
    crypt_text = ""
    for letter in text:
        if letter in cypher.keys():
            crypt_text += (cypher[letter])
        else:
            crypt_text += letter
    return crypt_text


def main(text: str, step: int):
    
    pass


if __name__ == '__main__':
    message_encrypt = 'Hello, World!'
    message_decrypt = 'Khoor, Zruog!'
    step_ = 3
    print(f"Decrypted: {encrypt_message(message_decrypt, step_, True)}")
    print(f"Encrypted: {encrypt_message(message_encrypt)}")
    