import module.utils
from module.Classification_module.cl_basic import cl_basic
from module.Classification_module.target import target_detect
from module.Classification_module.cl_sub import cl_sub
from pprint import pprint

def classification(parsed_text):
  classification_main_result =  cl_basic(parsed_text)
  if len(classification_main_result) == 3:
    status = classification_main_result.pop(2)
  elif len(classification_main_result) == 2:
    status = classification_main_result.pop(1)
  else:
    exit()
  target = target_detect(parsed_text)
  classification_sub_result = cl_sub(classification_main_result[0],parsed_text)
  result = {
    "basic_classification":classification_main_result,
    "sub_classification":classification_sub_result,
    "status":status,
    "target":target,
  }
  return result

def input_csv():
  data = utils.open_csv(input('file_name>'))
  for row in data:
    print(row)
    print(classification(utils.split_words(row)))
    print("-------------------------")
    input('next...')

def main():
  text = input('text>')
  parsed_text = utils.split_words(text)
  pprint(classification(parsed_text))

if __name__ == "__main__":
  while True:
    #main()
    input_csv()