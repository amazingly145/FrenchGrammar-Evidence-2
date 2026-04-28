import nltk
from nltk import CFG

## Grammar found
grammar = CFG.fromstring("""
    S -> NP
    NP -> F NPP 
    NPP -> E NPP | 
    E -> CONJ F
    F -> Pron B
    B -> Verb C
    C -> Det COD

    Pron -> 'Je' | 'Tu' | 'Il' | 'Elle' | 'Nous' | 'Vous' | 'Ils' | 'Elles'
    CONJ -> 'et' | 'ou'
    Verb -> 'etre' | 'avoir' | 'mange' | 'regarde' | 'parler' | 'aime' | 'parle' | 'ecoute' | 'chante'
    COD -> 'film' | 'pomme' | 'musique' | 'orange' | 'pizza' | 'peinture' | 'maison' | 'gateau' | 'salade' | 'livre' | 'francais' | 'chanson' | 'radio' | 'tableau'
    Det -> 'le' | 'la' | 'une' | 'un'
""")
parser = nltk.ChartParser(grammar)

# We prove the following sentences
correct_sentences = [
    "Je mange une pomme et Tu aime la musique",
    "Il regarde un film ou Elle ecoute une chanson",
    "Nous parle un francais et Vous mange une salade",
    "Ils chante une chanson ou Elles regarde un tableau",
    "Je ecoute une radio et Il mange un gateau",
    "Tu regarde un film ou Nous aime une pizza",
    "Elle chante un livre et Ils parle un francais",
    "Vous mange une salade ou Je regarde un tableau",
    "Il aime une pomme et Elle ecoute une chanson",
    "Nous mange un gateau ou Tu chante une radio",
]

incorrect_sentences = [
    "un pomme mange Je et un pizza mange Tu",
    "la musique aime Tu ou le film regarde Il",
    "une chanson ecoute Elle et une radio chante Nous",
    "un gateau mange Vous ou un tableau regarde Ils",
    "une pomme mange Je et Tu aime la musique",
    "un film regarde Il ou Elle ecoute une chanson",
    "la pizza aime Tu et Nous parle un francais",
    "Je mange une pomme et la musique aime Tu",
    "Il regarde un film ou une chanson ecoute Elle",
    "Tu aime la pizza et un francais parle Nous",
    "Je pomme mange une et Tu musique aime la",
    "Il film regarde un ou Elle chanson ecoute une",
]

print("==================================")
print("Correct sentences test")
print("==================================")
# The string is accepted if a tree is found
for i in range(len(correct_sentences)):
    tokens = correct_sentences[i].split()
    trees = list(parser.parse(tokens))
    status = "ACCEPTED" if len(trees) > 0 else "REJECTED"
    print("[" + status + "] " + correct_sentences[i])

print()
print("==================================")
print("INCORRECT SENTENCES")
print("==================================")
# It is rejected if a tree is not found
for i in range(len(incorrect_sentences)):
    tokens = incorrect_sentences[i].split()
    trees = list(parser.parse(tokens))
    status = "ACCEPTED" if len(trees) > 0 else "REJECTED"
    print("[" + status + "] " + incorrect_sentences[i])