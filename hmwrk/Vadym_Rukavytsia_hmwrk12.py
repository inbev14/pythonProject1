"""Encrypt or decrypt by the method of vertical permutation"""
import math
import random
import itertools
import re


# from prettytable import PrettyTable


def make_cypher(text: str, len_key: int) -> dict:
    """Encrypt message"""
    cypher = {}
    for key_i in range(1, len_key + 1):
        cypher.setdefault(key_i, [])
    count = 1
    for letter in text:
        if letter.isalnum():
            if count <= len_key:
                cypher[count].append(letter)
            elif count > len_key:
                count -= len_key
                cypher[count].append(letter)
            count += 1
    return cypher


def encoder(text: str, len_key: int) -> str:
    """working on cypher and convert to encoded text"""
    cypher = make_cypher(text, len_key)
    keys = list(cypher.keys())
    random.shuffle(keys)
    cryptogram = ''
    for one_key in keys:
        cryptogram += ''.join(cypher[one_key])
    return f'Cryptogram: {cryptogram}, key: {keys}'


def key_vars_generation(len_key: int):
    """Make keys combinations"""
    main_range = list(range(1, len_key + 1))
    vars_key = list(itertools.permutations(main_range, len_key))
    return vars_key


def decode(text: str, len_key: int, decode_key=None):
    """Decoding message with or without key"""
    formatted_text = ''.join(re.findall(r'\w', text))  # 'иеялптеблевебрмдяювдтю'
    not_round_y = len(formatted_text) / len_key  # = 4.4
    y_less = math.ceil(not_round_y) * len_key - len(formatted_text)  # = 3
    y_full = len(formatted_text) - math.floor(not_round_y) * len_key  # = 2
    # print(f'format text: {formatted_text}, not_roundY = {not_round_y}, y_less = {y_less}, y_full = {y_full}')
    combinations_dict = {}
    pattern1 = r'\w{math.floor(not_round_y)}{y_full}'
    pattern2 = r'\w{math.ceil(not_round_y)}{y_less}'
    if not decode_key:
        decode_key = key_vars_generation(len_key)
    else:
        decode_key = tuple(decode_key)
    for letter in formatted_text:
        pass
    
    

# def main(text: str, key: int) -> PrettyTable:
#     """Main controller"""
#     encrypted_text = encrypt_message(text, key)
#     table = PrettyTable()
#     table.field_names = ['Entered text', 'Return text', 'status']
#     # table.add_row([text, encrypted_text, 'decrypted' if decrypt else 'encrypted'])
#     return table


if __name__ == '__main__':
    text_ = 'привет медвед я тебя люблю'
    len_key_ = 5
    encoded_text = 'иеялптеблевебрмдяювдтю'
    key = (3, 1, 5, 2, 4)
    # encoded_text = 'lroiHMaeanlt'
    # decode(encoded_text, len_key_, key)
    # print(key_vars_generation(len_key_))
    # main(text)
    print(encoder(text_, len_key_))
    # Cryptogram: иеялптеблевебрмдяювдтю, key: (3, 1, 5, 2, 4)