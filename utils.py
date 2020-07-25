
import spacy

EXCEPTION_LIST  = ["ADP","AUX","PART","PUNCT", "NUM", "SYM"]
def split_words(text):
  nlp = spacy.load('ja_ginza')
  doc = nlp(text)
  exclusioned_text = []
  for sent in doc.sents:
    for token in sent:
      if token.pos_ in EXCEPTION_LIST :#and token.is_stop == True or token.pos_ == "PUNCT":
        if not str(token.orth_) == "？" or not str(token.lemma_) == "？":
          continue
      exclusioned_text.append(str(token.lemma_))
  return exclusioned_text
