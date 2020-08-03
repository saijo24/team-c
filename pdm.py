import psycopg2
import csv
import random
from classification import classification

slang_path = 'slang.txt'
conversation_path = 'conversation.txt'
template_co = "私は%sです"
template_opinion = "%sは%sだと思います"
template_slang = "%s"
template_conversation = "%s"

with open(slang_path,encoding='utf8') as f:
	slang = f.read().split(',')

with open(conversation_path,encoding='utf8') as f:
	conversation = f.read().split(',')
'''
connection = psycopg2.connect("host= port= dbname= user= password=")
cur =  connection.cursor()
cur.execute("use databases")
'''

#ラベル付け
text = "botさんの役職は何ですか？"
label = classification(text)

wolf = ["Aさん"]
myself = ["役職名"]

print(label)
if label["basic_classification"][0] == 'Coming_out':
	#co
	'''
	cur.execute("select jobs from self where username='bot'")
	myself = cur.fetchall()
	'''
	print(template_co % (myself[0]))   #CO
elif label["basic_classification"][0] == 'Opinion':
	#opinion
	'''
	cur.execute("select username from wolf orderby prob desc")
	wolf = cur.fetchall()
	'''
	print(template_opinion % (wolf[0],myself[0]))
elif label["basic_classification"][0] == 'Estimate':
	print("その推測は正しいと思います")
elif label["basic_classification"][0] == 'Agree':
	print("私もその意見に賛成です")
elif label["basic_classification"][0] == 'Disagree':
	print("なるほど")
else:
	#slang or conversation
	print(template_slang % (slang[random.randrange(len(slang))])) #slang
	print(template_conversation % (conversation[random.randrange(len(conversation))])) # conversation








