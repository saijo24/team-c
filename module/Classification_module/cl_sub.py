import sys
import os
sys.path.append(os.path.abspath(".."))
from module.utils import split_words
from module.Classification_module.target import target_detect,divined_target_detect

def cl_sub(basic_label,parsed_text):
  if basic_label in ["Coming_out","Estimate"]:
    return target_detect(parsed_text)
  elif basic_label == "Divined_inquested":
    return divined_target_detect(parsed_text)
  return None

def main():
  basic_label = input('basic_label>')
  text = input('text>')
  parsed_text = split_words(text)
  print(cl_sub(basic_label,parsed_text))

if __name__ == "__main__":
  while True:
    main()