print("Welcome to the pigLatin game")
message = input("Enter the English message to translate into pig latin: ")
vowels = ('a','e','i','o','u')
pigLatin = []
for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1] + suffixNonLetters
        word = word[:-1]

    wasUpper =word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    prefixConsonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefixConsonants += word[0]
        word = word[1:]

    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

print(' '.join(pigLatin))
