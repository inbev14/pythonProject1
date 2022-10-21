""" Julius Caesar's encryption machine in English, Ukrainian languages and cyrillic"""
from string import ascii_lowercase
from prettytable import PrettyTable
from rich.progress import track
import time


def choose_lang(lang: str) -> str:
    """Choosing language"""
    english = ['english', 'eng', 'en', 'usa', 'us', 'инглиш', 'англ', 'английский', 'англійська', 'інглиш', '']
    cyrillic = ['russian', 'rus', 'ru', 'ру', 'cyr', 'cy', 'rushka', 'русня', 'рашка', 'рус', 'кир', 'russia', 'раша']
    ukrainian = ['uk', 'ukr', 'ukrainian', 'укр', 'ук', 'українська', 'солов\'їна', 'ua', 'юа']
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


def anim_load_bar(decrypt=False):
    """Animation bar"""
    def scrape_data():
        time.sleep(0.005)
    if decrypt:
        for _ in track(range(100), description='[green]Decrypting in progress: '):
            scrape_data()
    else:
        for _ in track(range(100), description='[green]Encrypting in progress: '):
            scrape_data()


def encrypt_message(text: str, step=3, lang='en', decrypt=False) -> str:
    """Encrypting or decrypting message with step in ascii_letters"""
    cypher = make_cypher_key(step, lang)
    if decrypt:
        cypher = {letter: key for letter, key in cypher.items()}
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
    language = choose_lang(lang)
    if language == ENGLISH or language == CYRILLIC:
        step_message = 'Enter key for cypher (number, skip=3): '
        decrypt_message = 'Skip for encrypt and any key for decrypt message: '
        text_message = 'Enter your message: '
    elif language == UKRAINIAN:
        step_message = 'Введіть крок шифру (число, пропустити = 3): '
        decrypt_message = 'Пропусти щоб зашифрувати або введи будь-яку букву для розфирування: '
        text_message = 'Введи повідомлення: '
    step = input(step_message)
    if step.isnumeric():
        step = int(step)
    else:
        step = 3
    decrypt = bool(input(decrypt_message))
    text = input(text_message)
    return text, step, lang, decrypt


def main() -> PrettyTable:
    """Main controller"""
    text, step, lang, decrypt = data_collection()
    anim_load_bar(decrypt)
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
