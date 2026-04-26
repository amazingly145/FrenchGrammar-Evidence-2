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

print("Gramatica con ambiguedad y recursividad a la izquierda")
sentence = "Je aime la maison"
print(sentence)
tokens = sentence.split()

trees = list(parser.parse(tokens))

print("arboles:", len(trees))

for tree in trees:
    tree.pretty_print()


# Grammar without ambiguety and left recursion
grammar = CFG.fromstring("""
    S -> NP
    NP -> Pron B | A
    A -> D
    D -> NP E
    E -> CONJ F
    F -> Pron B
    B -> Verb C
    C -> Det COD

    Pron -> 'Je' | 'Tu' | 'Il' | 'Elle' | 'Nous' | 'Vous' | 'Ils' | 'Elles'
    CONJ -> 'et' | 'ou'
    Verb -> 'etre' | 'avoir' | 'mange' | 'regarde' | 'parler' | 'aime'
    COD -> 'film' | 'pomme' | 'musique' | 'orange' | 'pizza' | 'peinture' | 'maison'
    Det -> 'le' | 'la' | 'une' | 'un'
""")
parser = nltk.ChartParser(grammar)

print("Gramatica sin ambiguedad")
sentence = "Je mange une pomme et Tu aime la musique ou Il regarde le film"
tokens = sentence.split()

trees = list(parser.parse(tokens))

print("arboles:", len(trees))

for tree in trees:
    tree.pretty_print()