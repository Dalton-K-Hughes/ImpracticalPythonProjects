"""Map letters from string into dictionary & print bar chart of frequency."""

from collections import defaultdict
from pprint import pprint

def main():
    text = 'Like the castle in its corner in a medieval game, I foresee terrible trouble and I stay here just the same.'

    etaoin = defaultdict(list)

    for character in text.lower():
        if character.isalpha():
            etaoin[character].append(character)

    pprint(etaoin, width=110)

if __name__ == '__main__':
    main()