import numpy as np

DIACRITICAL = [('ę', 'ó', 'ą', 'ś', 'ł', 'ż', 'ź', 'ć', 'ń'), ('e', 'o', 'a', 's', 'l', 'z', 'x', 'c', 'n')]

pol = {
    'a': 9.9,
    'b': 1.47,
    'c': 4.36,
    'd': 3.25,
    'e': 8.77,
    'f': 0.30,
    'g': 1.42,
    'h': 1.08,
    'i': 8.21,
    'j': 2.28,
    'k': 3.51,
    'l': 3.92,
    'm': 2.80,
    'n': 5.72,
    'o': 8.6,
    'p': 3.13,
    'q': 0.14,
    'r': 4.69,
    's': 4.98,
    't': 3.98,
    'u': 2.50,
    'v': 0.04,
    'w': 4.65,
    'x': 0.02,
    'y': 3.76,
    'z': 6.53
}
en = {
    'a': 8.2,
    'b': 1.5,
    'c': 2.8,
    'd': 4.3,
    'e': 13,
    'f': 2.2,
    'g': 2,
    'h': 6.1,
    'i': 7,
    'j': 0.15,
    'k': 0.77,
    'l': 4,
    'm': 2.4,
    'n': 6.7,
    'o': 7.5,
    'p': 1.9,
    'q': 0.095,
    'r': 6,
    's': 6.3,
    't': 9.1,
    'u': 2.8,
    'v': 0.98,
    'w': 2.4,
    'x': 0.15,
    'y': 2,
    'z': 0.075
}
ger = {
    'a': 6.516,
    'b': 1.886,
    'c': 2.732,
    'd': 5.076,
    'e': 16.396,
    'f': 1.656,
    'g': 3.009,
    'h': 4.577,
    'i': 6.550,
    'j': 0.268,
    'k': 1.417,
    'l': 3.437,
    'm': 2.534,
    'n': 9.776,
    'o': 2.594,
    'p': 0.670,
    'q': 0.018,
    'r': 7.003,
    's': 7.270,
    't': 6.154,
    'u': 4.166,
    'v': 0.746,
    'w': 1.921,
    'x': 0.034,
    'y': 1.039,
    'z': 1.134
}
pol_vow_cons = {'vowels': 37.980000000000004, 'consonants': 62.029999999999994}
en_vow_cons = {'vowels': 38.5, 'consonants': 61.91999999999999}
ger_vow_cons = {'vowels': 36.221999999999994, 'consonants': 62.357000000000006}

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def remove_diacritical(text: str) -> str:
    for i, char in enumerate(DIACRITICAL[0]):
        text = text.replace(char, DIACRITICAL[1][i])
    return text


def closest_lang(text: str) -> None:
    text = remove_diacritical(text).lower()
    letter_freq = {}
    for letter in letters:
        letter_freq[letter] = text.count(letter) / len(text) * 100
    en_diff = [x1 - x2 for (x1, x2) in zip(letter_freq.values(), en.values())]
    pol_diff = [x1 - x2 for (x1, x2) in zip(letter_freq.values(), pol.values())]
    ger_diff = [x1 - x2 for (x1, x2) in zip(letter_freq.values(), ger.values())]
    en_dist = np.linalg.norm(en_diff)
    pol_dist = np.linalg.norm(pol_diff)
    ger_dist = np.linalg.norm(ger_diff)
    dist = [en_dist, pol_dist, ger_dist]
    min_dist = min(dist)
    if min_dist == en_dist:
        print('Najbardziej podobny język na podstawie częstośći występowania liter to angielski')
        return
    if min_dist == pol_dist:
        print('Najbardziej podobny język na podstawie częstośći występowania liter to polski')
        return
    if min_dist == ger_dist:
        print('Najbardziej podobny język na podstawie częstośći występowania liter to niemiecki')
        return
    return


def closest_by_vowels_and_consonants(text: str) -> None:
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = remove_diacritical(text).lower()
    vowels_sum = 0
    for vowel in vowels:
        vowels_sum += text.count(vowel)
    vowels_percentage = vowels_sum / len(text) * 100
    consonants_percentage = 100 - vowels_percentage
    vow_con = [vowels_percentage, consonants_percentage]
    en_diff = [x1 - x2 for (x1, x2) in zip(vow_con, en_vow_cons.values())]
    pol_diff = [x1 - x2 for (x1, x2) in zip(vow_con, pol_vow_cons.values())]
    ger_diff = [x1 - x2 for (x1, x2) in zip(vow_con, ger_vow_cons.values())]
    en_dist = np.linalg.norm(en_diff)
    pol_dist = np.linalg.norm(pol_diff)
    ger_dist = np.linalg.norm(ger_diff)
    dist = [en_dist, pol_dist, ger_dist]
    min_dist = min(dist)
    if min_dist == en_dist:
        print('Najbardziej podobny język na podstawie spółgłosek i samogłosek to angielski')
        return
    if min_dist == pol_dist:
        print('Najbardziej podobny język na podstawie spółgłosek i samogłosek to polski')
        return
    if min_dist == ger_dist:
        print('Najbardziej podobny język na podstawie spółgłosek i samogłosek to niemiecki')
        return


with open('ger.txt', 'r', encoding='utf-8') as german:
    print('\nJęzyk tekstu: Niemiecki')
    _text = german.read()
    closest_lang(_text)
    closest_by_vowels_and_consonants(_text)

with open('pol.txt', 'r', encoding='utf-8') as polish:
    print('\nJęzyk tekstu: Polski')
    _text = polish.read()
    closest_lang(_text)
    closest_by_vowels_and_consonants(_text)

with open('eng.txt', 'r', encoding='utf-8') as english:
    print('\nJęzyk tekstu: Angielski')
    _text = english.read()
    closest_lang(_text)
    closest_by_vowels_and_consonants(_text)
print('-----')
_text = 'dzisiaj jest poniedziałek'
closest_lang(_text)
closest_by_vowels_and_consonants(_text)
