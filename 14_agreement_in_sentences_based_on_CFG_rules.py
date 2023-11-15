import nltk
# from nltk import ParseError
nltk.download('punkt')
nltk.download('stopwords')

grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | VP PP
PP -> Prep NP
NP -> Det N | N PP
Det -> The | A
N -> dog | cat | fox
V -> jumps | runs | sleeps
Prep -> in | on | under
A -> big | small
""")


def check_agreement(sentence):

    tokens = nltk.word_tokenize(sentence)

    # Parse the sentence
    try:
        parser = nltk.ChartParser(grammar)
        tree = parser.parse(tokens)
    except nltk.ParseError:
        return False

    # Check for agreement between subject and verb
    for (subtree, label) in tree.subtrees():
        if label == 'NP' and subtree[0].label == 'Det':
            subject_number = subtree[1].label
        elif label == 'VP' and subtree[0].label == 'V':
            verb_number = subtree[0].label

        if subject_number == 'singular' and verb_number == 'plural':
            return False
        elif subject_number == 'plural' and verb_number == 'singular':
            return False

    return True


if __name__ == '__main__':
    sentence = "The big dog jumps over the lazy cat."
    is_grammatical = check_agreement(sentence)
    print("Sentence is grammatical:", is_grammatical)
