import nltk
from nltk.sem.logic import LogicParser

# Create a logic parser
logic_parser = LogicParser()

# Define some constants and variables
x = nltk.sem.Variable("x")
y = nltk.sem.Variable("y")

# Create FOL expressions
loves = logic_parser.parse('loves(x, y)')
hates = logic_parser.parse('hates(x, y)')

# Print the FOL expressions
print("FOL Expression 1:", loves)
print("FOL Expression 2:", hates)

# Create a negated expression using implication (->) and universal quantification
not_loves = logic_parser.parse('all x (loves(x, y) -> False)')

# Conjunction and disjunction are the same as before
and_expr = loves & hates
or_expr = loves | hates

# Print the results of FOL operations
print("Negation of Expression 1:", not_loves)
print("Conjunction of Expressions 1 and 2:", and_expr)
print("Disjunction of Expressions 1 and 2:", or_expr)
