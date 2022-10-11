from os import path, getcwd  # access
import re

filename = '../add_files/text_example.txt'


def find_longest_words(name_file):
    """Find the longest words and return length of them also list with the longest words"""
    file_path = path.join(getcwd(), name_file)
    with open(file_path) as file:
        words_text = sorted([word for word in re.findall(r'\w+', file.read())], key=len)
        highest_len_words = ", ".join([word for word in words_text if len(word) == len(words_text[-1])])
        
        # highest_len = 0
        # highest_len_words = []
        # file_text = re.split(r'[\W_]', file.read())
        # print(file_text)
        # for word in file_text:
        #     if len(word) >= highest_len:
        #         highest_len = len(word)
        # for word in file_text:
        #     if len(word) == highest_len:
        #         highest_len_words.append(word)
        return (f'You opened file {file_path}. \nThe longest words in "{name_file}" has {len(words_text[-1])} '
                f'symbols. The longest words are: {highest_len_words}.')
        # return finded_words


if __name__ == '__main__':
    print(find_longest_words(filename))
