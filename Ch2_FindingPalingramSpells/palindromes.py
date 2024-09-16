"""Find palindromes (letter palingrams) in a dictionary file"""

import load_dictionary
import os
print(os.listdir())
word_list = load_dictionary.load('Ch2_FindingPalingramSpells/2of12inf.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print('\nNumber of palindromes found = {}\n'.format(len(pali_list)))
print(*pali_list, sep='\n')