with open('/usr/share/dict/words') as word_list:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for w in (word.strip() for word in word_list if vowels < set(word)):
        print(w)
