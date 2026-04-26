import nltk
from nltk import CFG


# Grammar with ambiguety and left recursion
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
print("Gramatica sin ambiguedad")
print("Primera iteración para quitar la ambiguedad")
print("Se quita la ambiguedad en enunciados simples, pero no compuestas")
grammar = CFG.fromstring("""
S -> NP
    NP -> Pron B | A
    A -> D
    D -> NP E
    E -> CONJ NP
    B -> Verb C
    C -> Det COD

    Pron -> 'Je' | 'Tu' | 'Il' | 'Elle' | 'Nous' | 'Vous' | 'Ils' | 'Elles'
    CONJ -> 'et' | 'ou'
    Verb -> 'etre' | 'avoir' | 'mange' | 'regarde' | 'parler' | 'aime'
    COD -> 'film' | 'pomme' | 'musique' | 'orange' | 'pizza' | 'peinture' | 'maison'
    Det -> 'le' | 'la' | 'une' | 'un'
""")
parser = nltk.ChartParser(grammar)

print("Enunciado uno")
sentence = "Je mange une pomme"
tokens = sentence.split()

trees = list(parser.parse(tokens))

print("arboles:", len(trees))

for tree in trees:
    tree.pretty_print()

print("Enunciado 2")
sentence = "Je mange une pomme et Tu aime la musique ou Il regarde le film"
tokens = sentence.split()

trees = list(parser.parse(tokens))

print("arboles:", len(trees))

for tree in trees:
    tree.pretty_print()

print("Segunda iteración para quitar la ambiguedad")
print("Se quita la ambiguedad en enunciados simples y compuestas")
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

print("Enunciado uno")
sentence = "Je mange une pomme"
tokens = sentence.split()

trees = list(parser.parse(tokens))

print("arboles:", len(trees))

for tree in trees:
    tree.pretty_print()

print("Enunciado 2")
sentence = "Je mange une pomme et Tu aime la musique ou Il regarde le film"
tokens = sentence.split()

trees = list(parser.parse(tokens))

print("arboles:", len(trees))

for tree in trees:
    tree.pretty_print()