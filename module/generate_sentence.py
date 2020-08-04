#import psycopg2
import csv
import random
from module.classification import classification

slang_path = 'module/slang.txt'
conversation_path = 'module/conversation.txt'
template_co = "私は%sです"
template_opinion = "%sは%sだと思います"
template_slang = "%s"
template_conversation = "%s"
wolf = ["Aさん"]
myself = ["役職名"]

def init():
  with open(slang_path,encoding='utf8') as f:
    slang = f.read().split(',')

  with open(conversation_path,encoding='utf8') as f:
    conversation = f.read().split(',')
  return slang,conversation
'''
connection = psycopg2.connect("host= port= dbname= user= password=")
cur =  connection.cursor()
cur.execute("use databases")
'''

#ラベル付け

def generation_sentence(label):
  slang,conversation = init()
  sentence = ""
  if label["basic_classification"][0] == 'Coming_out':
    #co
    '''
    cur.execute("select jobs from self where username='bot'")
    myself = cur.fetchall()
    '''
    sentence = template_co % (myself[0])  #CO
  elif label["basic_classification"][0] == 'Opinion':
    #opinion
    '''
    cur.execute("select username from wolf orderby prob desc")
    wolf = cur.fetchall()
    '''
    sentence = template_opinion % (wolf[0],myself[0])
  elif label["basic_classification"][0] == 'Estimate':
    sentence = "その推測は正しいと思います"
  elif label["basic_classification"][0] == 'Agree':
    sentence = "私もその意見に賛成です"
  elif label["basic_classification"][0] == 'Disagree':
    sentence = "なるほど"
  else:
    #slang or conversation
    sentence = str(template_slang % (slang[random.randrange(len(slang))])) #slang
    sentence =str(template_conversation % (conversation[random.randrange(len(conversation))])) # conversation
  return sentence

def main():
  text = "botさんの役職は何ですか？"
  label = classification(text)
  print(text)
  print(generation_sentence(label))

if __name__ == "__main__":
  main()