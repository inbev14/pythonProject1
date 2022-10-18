""" Julius Caesar's encryption machine in English, Ukrainian and rushka languages"""
from string import ascii_lowercase
from prettytable import PrettyTable
import time


def choose_lang(lang: str) -> str:
    """Choosing language"""
    english = ['english', 'eng', 'en', 'usa', 'us', 'инглиш', 'англ', 'английский', 'англійська', 'інглиш', '']
    cyrillic = ['russian', 'rus', 'ru', 'ру', 'cyr', 'cy', 'rushka', 'русня', 'рашка', 'рус', 'кир', 'russia', 'раша']
    ukrainian = ['uk', 'ukr', 'ukrainian', 'укр', 'ук', 'українська', 'солов\'їна', 'ua']
    if lang in english:
        return ENGLISH
    elif lang in ukrainian:
        return UKRAINIAN
    elif lang in cyrillic:
        return CYRILLIC
    print(f'Language "{lang}" is unsupported yet.')
    exit()


def make_cypher_key(step: int, lang: str) -> dict:
    """Making cypher key dictionary with step"""
    alphabet = choose_lang(lang)
    cypher = {}
    for number, letter in enumerate(alphabet, step):
        if number < len(alphabet):
            cypher[letter] = alphabet[int(number)]
        else:
            cypher[letter] = alphabet[int(number) - len(alphabet)]
    return cypher


def loading_anim():
    """Animation loading"""
    animation = "|/-\\"
    idx = 0
    while idx < 15:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)


def encrypt_message(text: str, step=3, lang='en', decrypt=False):
    """Encrypting or decrypting message with step in ascii_letters"""
    cypher = make_cypher_key(step, lang)
    if decrypt:
        cypher = {cypher[let]: let for let in cypher}
    encrypted_text = ""
    for letter in text:
        if letter.lower() in cypher.keys():
            if letter.isupper():
                encrypted_text += str((cypher[letter.lower()])).upper()
            else:
                encrypted_text += (cypher[letter])
        else:
            encrypted_text += letter
    return encrypted_text


def data_collection():
    """Collect data from user"""
    lang = input('Enter language (default="en" or "ua","ru"): ')
    step = input('Enter key for cypher (number): ')
    if step.isnumeric():
        step = int(step)
    else:
        step = 3
    decrypt = bool(input('Skip for encrypt and any key for decrypt message: '))
    text = input("Enter your message: ")
    return text, step, lang, decrypt


def main():
    """Main controller"""
    text, step, lang, decrypt = data_collection()
    loading_anim()
    encrypted_text = encrypt_message(text, step, lang, decrypt)
    table = PrettyTable()
    table.field_names = ['Entered text', 'Return text', 'status']
    table.add_row([text, encrypted_text, 'decrypted' if decrypt else 'encrypted'])
    return table


ENGLISH = ascii_lowercase
UKRAINIAN = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
CYRILLIC = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

if __name__ == '__main__':
    print(main())
    message_encrypted = 'Khoor, Zruog!'
    message_decrypted = 'Hello, World!'
    
    assert message_encrypted == encrypt_message(message_decrypted)
    assert message_decrypted == encrypt_message(message_encrypted, decrypt=True)
    
    # message_ua = 'Привіт, Як у Тебе справи?'
  
