from os import path, getcwd   # access


filename = 'text_example.txt'


def find_longest_words(name_file):
    """Find the longest words and return length of them also list with the longest words"""
    file_path = path.join(getcwd(), 'other_files', name_file)
    with open(file_path) as file:
        highest_len = 0
        highest_len_words = []
        file_text = file.read().split()
        for word in file_text:
            if len(word) >= highest_len:
                highest_len = len(word)
        for word in file_text:
            if len(word) == highest_len:
                highest_len_words.append(word)
        return (f'You opened file {file_path}. \nThe longest words in "{name_file}" has {highest_len} symbols.'
                f' The longest words are: {highest_len_words}.')
    
print(find_longest_words(filename))