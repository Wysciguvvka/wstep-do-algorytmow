import string
from typing import Callable
from functools import partial

DIACRITICAL = [('ę', 'ó', 'ą', 'ś', 'ł', 'ż', 'ź', 'ć', 'ń'), ('e', 'o', 'a', 's', 'l', 'z', 'x', 'c', 'n')]
NEARBY_CHARS = {
    "q": ["w", "s", "ś", "a", "ą", "1", "!", "2", "@"],
    "w": ["q", "e", "ę", "d", "s", "ś", "a", "ą", "2", "@", "3", "#"],
    "e": ["w", "r", "f", "d", "s", "ś", "3", "#", "4", "$", "ę"],
    "r": ["e", "ę", "t", "g", "f", "d", "4", "$", "5", "%"],
    "t": ["r", "y", "f", "g", "h", "5", "%", "6", "^"],
    "y": ["t", "u", "g", "h", "j", "6", "^", "7", "&"],
    "u": ["y", "i", "k", "j", "h", "7", "&", "8", "*"],
    "i": ["u", "o", "ó", "l", "ł", "k", "j", "8", "*", "9", "("],
    "o": ["i", "p", "l", ";", ":", "ł", "k", "ó"],
    "p": ["o", "ó", "[", "{", "'", '"', ";", ":", "l", "ł"],
    "a": ["q", "w", "s", "ś", "x", "ź", "z", "ż", "ą"],
    "s": ["q", "w", "e", "ę", "d", "c", "ć", "x", "ź", "z", "ż", "a", "ą"],
    "d": ["s", "ś", "w", "e", "ę", "r", "f", "v", "c", "ć", "x", "ź"],
    "f": ["d", "e", "ę", "r", "t", "g", "b", "v", "c", "ć"],
    "g": ["f", "r", "t", "y", "h", "n", "ń", "b", "v"],
    "h": ["g", "t", "y", "u", "j", "m", "n", "ń", "b"],
    "j": ["h", "y", "u", "i", "k", ",", "<", "m", "n", "ń"],
    "k": ["j", "u", "i", "o", "ó", "l", "ł", ".", ">", ",", "<", "m"],
    "l": ["k", "i", "o", "ó", "p", ";", ":", "/", "?", ".", ">", ",", "<", "ł"],
    "z": ["a", "ą", "s", "ś", "d", "x", "ź", "ż"],
    "x": ["z", "ż", "a", "ą", "s", "ś", "d", "c", "ć", "ź"],
    "c": ["x", "ź", "s", "ś", "d", "f", "v", "ć"],
    "v": ["c", "ć", "d", "f", "g", "b"],
    "b": ["v", "f", "g", "h", "n", "ń"],
    "n": ["b", "g", "h", "j", "m", "ń"],
    "m": ["n", "ń", "j", "k", "l", "ł", ",", "<"],
}

wordlist = [
    "flota",
    "enzym",
    "kurczak",
    "krab",
    "emigrant",
    "rosja",
    "piknik",
    "cel",
    "syrena",
    "beton",
    "unia",
    "ankieta",
    "kopiarka",
    "cyrk",
    "zysk",
    "stanik",
    "dziennikarz",
    "podpis",
    "curry",
    "przyczepa",
    "termit",
    "banan",
    "wsparcie",
    "waga",
    "licencja",
    "wybawca",
    "piosenka",
    "kamyk",
    "hazard",
    "spadochron",
    "plakat",
    "energia",
    "bilans",
    "wzmacniacz",
    "peleryna",
    "klakson",
    "wojna",
    "balkon",
    "aluminium",
    "bestia",
    "dziecko",
    "planowanie",
    "plakat",
    "biedronka",
    "kominek",
    "ranek",
    "jaskinia",
    "strategia",
    "akta",
    "tartan",
    "papier",
    "ogon",
    "groszek",
    "fryzjer",
    "higiena",
    "szpital",
    "region",
    "marmur",
    "gaz",
    "zajazd",
    "egipt",
    "mewa",
    "kangur",
    "krew",
    "renifer",
    "szminka",
    "akwarium",
    "cyrk",
    "uczta",
    "duch",
    "piwnica",
    "tron",
    "emerytura",
    "rana",
    "korporacja",
    "stokrotka",
    "skrzynka",
    "telefon",
    "parada",
    "oliwka",
    "gruszka",
    "bakteria",
    "biblia",
    "syrena",
    "kolana",
    "spadochron",
    "prawnik",
    "wina",
    "nerka",
    "futro",
    "dym",
    "karta",
    "okulary",
    "maska",
    "wdowa",
    "klucz",
    "tost",
    "sterta",
    "pineska",
    "obrazek",
]


def remove_diacritical(text: str) -> str:
    for i, char in enumerate(DIACRITICAL[0]):
        text = text.replace(char, DIACRITICAL[1][i])
    return text


def hamming(_s1: str, _s2: str, printing: bool = False) -> int:
    result = 0
    s1 = remove_diacritical(_s1)
    s2 = remove_diacritical(_s2)
    if len(s1) != len(s2):
        print("Podane słowa nie są równej długości")
        return -1
    for x, (i, j) in enumerate(zip(s1, s2)):
        if i != j:
            if printing:
                print(f'Nie zgadza się znak {_s1[x], _s2[x]} na miejscu {x}')
            result += 1
    if printing:
        print(f'Podobieństwo wyrazów {_s1} i {_s2}: {result}')
    return result


def kb_distance(_s1: str, _s2: str, printing: bool = False) -> int:
    result = 0
    s1 = remove_diacritical(_s1)
    s2 = remove_diacritical(_s2)
    if len(s1) != len(s2):
        print("Podane słowa nie są równej długości")
        return -1
    for x, (i, j) in enumerate(zip(s1, s2)):
        if i != j:
            if printing:
                print(f'Nie zgadza się znak {_s1[x], _s2[x]} na miejscu {x}')
            result += 1 if i in NEARBY_CHARS[j] else 2
    if printing:
        print(f'Podobieństwo wyrazów {_s1} i {_s2}: {result}')
    return result


def search_in_wl(
        query, comp_method: Callable[[str, str], int] = hamming
) -> None:
    if query in wordlist:
        print(f"Znaleziono {query} na liście słów!")
        return
    part = partial(comp_method, query)
    matching_lens = [w for w in wordlist if len(w) == len(query)]
    matching_lens.sort(key=part)
    if matching_lens:
        print(f"Nie znaleziono wyrazu {query}. Najbliższe słowa to: {', '.join(matching_lens[0:3])}")
    else:
        print(f"Nie znaleziono wyrauz oraz podobnych słów.")


print('odległość Hamminga:')
hamming('mama', 'nawa', True)
print('odległość Hamminga - modyfikacja:')
kb_distance('mama', 'nawa', True)
print('najbliższe słowa do nawa:')
search_in_wl('nawa')
