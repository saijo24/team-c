import sys
import os
sys.path.append(os.path.abspath(".."))
from module.utils import split_words

ROLE = {
  0:"Citizen",
  1:"Diviner",
  2:"Medium",
  3:"Co-owner",
  4:"Hunter",
  5:"Madman",
  6:"Wolf",
  7:"Hamster",
}

TARGET_TEXT = [
  ["市民"],
  ["占い師"],
  ["霊媒師"],
  ["共有"],
  ["狩人"],
  ["狂人"],
  ["人狼"],
  ["ハムスター"]
]

DIVINED_TEXT = [
  ["白","市民"],
  ["黒","人狼","人狼陣営"]
]

def target_detect(parsed_text):
  for sent in parsed_text:
    i = 0
    for target_text_list  in TARGET_TEXT:
      if sent in target_text_list:
        return ROLE[i]
      else:
        i+=1
  return None

def divined_target_detect(parsed_text):
  for sent in parsed_text:
    i = 0
    for target_text_list in DIVINED_TEXT:
      if sent in target_text_list:
        if i == 0:
          return "Citizen"
        elif i == 1:
          return "Wolf"
      i+=1
  return None



def main():
  text = input('text>')
  parsed_text = split_words(text)
  print(target_detect(parsed_text))
  print(divined_target_detect(parsed_text))

if __name__ == "__main__":
  while True:
    main()