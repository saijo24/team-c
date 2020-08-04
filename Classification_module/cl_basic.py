import random
from pprint import pprint

TAG = {1:"Coming_out",2:"Divined_inquested",3:"Guard",4:"Vote",5:"Estimate",6:"Agree",7:"Disagree",8:"Opinion",9:"Information",10:"Question",11:"Ans",12:"Request"}
BODER = 0.7
def classification(data):
  result = {
    1:random.random(),
    2:random.random(),
    3:random.random(),
    4:random.random(),
    5:random.random(),
    6:random.random(),
    7:random.random(),
    8:random.random(),
    9:random.random(),
    10:random.random(),
    11:random.random(),
    12:random.random(),
  }
  return result

def cl_basic(data):
  result = []
  i = 0
  classification_result = classification(data)
  sorted_result = sorted(classification_result.items(), key=lambda x:x[1],reverse=True)
  for key in sorted_result:
    if i == 0:
      result.append(TAG[key[0]])
      i+=1
    elif i ==1 and key[1] >= BODER and key[0] not in [6,7]:
      result.append(TAG[key[0]])
      break
  if classification_result[6] >= classification_result[7]:
    result.append("Agree")
  else:
    result.append("Disagree")
  return result

def main():
  print(cl_basic("test"))
if __name__ == "__main__":
  main()