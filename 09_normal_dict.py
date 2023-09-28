word_features = {
    'category':'Noun',
    'person' : '3rd',
    'number' : 'singular'
}
for feature,value in word_features.items():
  print(f"{feature} : {value}")

another_word_features = {
    'category':'Verb',
    'person' : '1st',
    'number' : 'singular'
}
for feature,value in another_word_features.items():
  print(f"{feature} : {value}")
