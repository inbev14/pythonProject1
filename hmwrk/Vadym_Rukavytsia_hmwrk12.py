"""Encrypt or decrypt by the method of vertical permutation"""
import random
from prettytable import PrettyTable


def make_cypher(text: str, key: int) -> dict:
    """Encrypt message"""
    cypher = {}
    for key_i in range(1, key + 1):
        cypher.setdefault(key_i, [])
    count = 1
    for letter in text:
        if letter.isalnum():
            if count <= key:
                cypher[count].append(letter)
            elif count > key:
                count -= key
                cypher[count].append(letter)
            count += 1
    return cypher


def encoder(text: str, len_key: int) -> str:
    """working on cypher and convert to encoded text"""
    cypher = make_cypher(text, len_key)
    keys = list(cypher.keys())
    random.shuffle(keys)
    cryptogram = ''
    for key in keys:
        cryptogram += ''.join(cypher[key])
    return f'Cryptogram: {cryptogram}, key: {keys}'

def decoder(text: str, key: int):
    pass
    
    

# def main(text: str, key: int) -> PrettyTable:
#     """Main controller"""
#     encrypted_text = encrypt_message(text, key)
#     table = PrettyTable()
#     table.field_names = ['Entered text', 'Return text', 'status']
#     # table.add_row([text, encrypted_text, 'decrypted' if decrypt else 'encrypted'])
#     return table


if __name__ == '__main__':
    text_ = 'Hello Martian'
    key_ = 5
    encoded_text = 'lroiHMaeanlt'
    # main(text)
    print(encoder(text_, key_))
