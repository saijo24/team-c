import module.utils as utils
from module.classification import classification
from module.generate_sentence import generation_sentence
from pprint import pprint

def debug(data):
  for row in data:
    parsed_text = utils.split_words(row)
    if parsed_text == []:
      continue
    label = classification(parsed_text)
    sentence = generation_sentence(label)
    print("text : " + row)
    print("label : ")
    pprint(label)
    print("Suggestion : " + sentence)
    input('next.....')
    print("========================================")

def main():
  file = input('file>')
  data = utils.open_csv(file)
  debug(data)

if __name__ == "__main__":
  main()