from nltk import CFG, PCFG, ViterbiParser
import nltk

pcfg_grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.7] | Pronoun [0.3]
VP -> V NP [0.9] | VP PP [0.1]
PP -> P NP [1.0]
Det -> 'the' [0.2] | 'a' [0.3] | 'an' [0.5]  
Pronoun -> 'I' [0.4] | 'You' [0.3] | 'he' [0.2] | 'she' [0.1]  
V -> 'chased' [0.5] | 'saw' [0.5]
P -> 'with' [0.6] | 'in' [0.4]
N -> 'cat' [0.3] | 'dog' [0.3] | 'bat' [0.4]  
""")
parser = ViterbiParser(pcfg_grammar)
sent = "the cat chased the dog with a bat"
tokens = sent.split()
parsed_trees = list(parser.parse(tokens))
for tree in parsed_trees:
    tree.pretty_print()
most_likely_parse = parsed_trees[0]
print("PCFG Output : ", most_likely_parse.prob())
