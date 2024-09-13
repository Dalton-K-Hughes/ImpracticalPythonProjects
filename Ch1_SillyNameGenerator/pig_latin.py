'''A program that will transform a word into Pig Latin.'''


def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    word = input("Please enter a word: \n")

    if word[0] not in vowels:
        word = word[1:] + word[0] + 'ay'
    else:
        word = word + 'way'

    print(word)

if __name__ == '__main__':
    main()