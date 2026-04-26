import nltk
from nltk import CFG


# Grammar with ambiguery and left recursion
grammar = CFG.fromstring("""
    S -> NP
    NP -> Pron B | A
    A -> NP CONJ NP | NP
    B -> Verb C
    C -> Det COD

    Pron -> 'Je' | 'Tu' | 'Il' | 'Elle' | 'Nous' | 'Vous' | 'Ils' | 'Elles'
    CONJ -> 'et' | 'ou'
    Verb -> 'etre' | 'avoir' | 'mange' | 'regarde' | 'parler' | 'aime'
    COD -> 'film' | 'pomme' | 'musique' | 'orange' | 'pizza' | 'peinture' | 'maison'
    Det -> 'le' | 'la' | 'une' | 'un'
""")
parser = nltk.ChartParser(grammar)

sentence = "Je aime la maison"
tokens = sentence.split()

trees = list(parser.parse(tokens))

print("arboles:", len(trees))

for tree in trees:
    tree.pretty_print()


# Grammar without ambiguety and left recursion
grammar = CFG.fromstring("""
    S -> NP
    NP -> Pron B | A
    A -> NP CONJ NP | NP
    B -> Verb C
    C -> Det COD

    Pron -> 'Je' | 'Tu' | 'Il' | 'Elle' | 'Nous' | 'Vous' | 'Ils' | 'Elles'
    CONJ -> 'et' | 'ou'
    Verb -> 'etre' | 'avoir' | 'mange' | 'regarde' | 'parler' | 'aime'
    COD -> 'film' | 'pomme' | 'musique' | 'orange' | 'pizza' | 'peinture' | 'maison'
    Det -> 'le' | 'la' | 'une' | 'un'
""")
parser = nltk.ChartParser(grammar)

sentence = "Je aime la maison et Tu aime la maison"
tokens = sentence.split()

trees = list(parser.parse(tokens))

print("arboles:", len(trees))

for tree in trees:
    tree.pretty_print()