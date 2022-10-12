"""Converting a phrase to a sequence of numbers T9"""


def letter_to_num(letter: str) -> str:
    """Takes a letter and returns a digital analog of the letter"""
    keyboard = {0: ' 0', 1: '.,?!:1', 2: 'abc2', 3: 'def3', 4: 'ghi4', 5: 'jkl5', 6: 'mno6', 7: 'pqrs7', 8: 'tuv8',
                9: 'wxyz9'}
    for number, symbols in keyboard.items():
        if letter in symbols:
            t9_symbol = str(number) * (symbols.index(letter) + 1)
            return t9_symbol
    return ''


def main(phrase: str) -> str:
    """Main controller"""
    t9_phrase = ''
    for letter in phrase.lower():
        t9_phrase += (letter_to_num(letter))
    return t9_phrase


if __name__ == '__main__':
    text = 'jkl'
    print(main(text))
    assert main('ad g') == '2304'
    assert main('Hello, World!') == '4433555555666110966677755531111'
    assert main('Heavy METAL!') == '443328889990633825551111'
