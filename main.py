import utils
from Classification_module.cl_basic import cl_basic

def classification(parsed_text):
  classification_main_result =  cl_basic(parsed_text)
  status =classification_main_result.pop(2)
  result = {
    "basic_classification":classification_main_result,
    "status":status,
  }
  return result

def main():
  text = input('text>')
  parsed_text = utils.split_words(text)
  print(classification(parsed_text))

if __name__ == "__main__":
  while True:
    main()