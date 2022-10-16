from string import ascii_lowercase

letters = ascii_lowercase
shift_step = 3
phrase = 'hi'


def generator(number: int):
    print('work')
    mylist = range(number)
    for el in mylist:
        yield el

for i in range(3):
    print(i)

for i in generator(3):
    print(i)
for i in generator(3):
    print(i)
    