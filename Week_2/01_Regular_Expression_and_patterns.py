import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California. It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976."

# Process the text with spaCy
doc = nlp(text)

# Extract named entities (e.g., organization names and dates)
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")

# Extract sentences
print("\nSentences:")
for sent in doc.sents:
    print(sent.text)
