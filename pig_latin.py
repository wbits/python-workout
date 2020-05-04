vowels = 'aeiouAEIOU'


def ay(word: str) -> str:
    return f'{word[1:]}{word[0]}ay'


def way(word: str) -> str:
    return f'{word}way'


def translate_pig_latin(word: str) -> str:
    if word[0] in vowels:
        return way(word)

    return ay(word)


def translate_ubbi_dubbi(word: str) -> str:
    output = []
    for char in word:
        if char in vowels:
            output.append(f'ub{char}')
        else:
            output.append(char)

    return ''.join(output)


def translate_sentence(sentence: str) -> str:
    return ' '.join(map(translate_ubbi_dubbi, sentence.split()))


def prompt():
    print(translate_sentence(input('Enter a sentence ')))

    if input('Again y/n? ') == 'y':
        prompt()

    print('tsiao....')

    exit(0)


prompt()
