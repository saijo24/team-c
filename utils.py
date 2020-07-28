import spacy
import csv

EXCEPTION_LIST  = ["ADP","AUX","PART","PUNCT", "NUM", "SYM"]

def open_csv(file):
  tmp = []
  with open(file,encoding='shift-jis') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
  for i in range(len(data)): tmp.append(data[i][3])
  return tmp
  
def split_words(text):
  nlp = spacy.load('ja_ginza')
  doc = nlp(text)
  exclusioned_text = []
  for sent in doc.sents:
    for token in sent:
      if token.pos_ in EXCEPTION_LIST:
        if not str(token.orth_) == "？" or not str(token.lemma_) == "？":
          continue
      exclusioned_text.append(str(token.lemma_))
  return exclusioned_text
