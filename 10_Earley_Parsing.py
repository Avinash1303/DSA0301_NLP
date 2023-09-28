import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP 
NP -> Det N 
VP -> V NP 
Det -> 'the' 
N -> 'dog'|'cat' 
V -> 'chased'|'ate'
""")
sent = "the dog chased the cat"
tokens = sent.split()
parser = nltk.EarleyChartParser(grammar)
for tree in parser.parse(tokens):
  print("Parse Tree:")
  print(tree)
  tree.pretty_print()
  print("\n")
