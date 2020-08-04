import csv
import glob
from time import sleep
from pprint import pprint
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import pickle
import os
import sys
import re
from chardet.universaldetector import UniversalDetector
import matplotlib.pyplot as plt
import optuna

TAG = {1:"Coming_out",2:"Divined_inquested",3:"Guard",4:"Vote",5:"Estimate",6:"Agree",7:"Disagree",8:"Opinion",9:"Information",10:"Question",11:"Ans",12:"Request",13:"None"}
TRAGET = {"param1":4,"param2":5,"param3":6}
exception_list = ["ADP","AUX","PART","PUNCT", "NUM", "SYM", "VARB"]
bar = None
X = None
Y = None

def split_words(text):
  nlp = spacy.load('ja_ginza')
  doc = nlp(text)
  global bar
  bar.update(1)
  exclusioned_text = []
  for sent in doc.sents:
    for token in sent:
      if token.pos_ in exception_list:#and token.is_stop == True or token.pos_ == "PUNCT":
        if not str(token.orth_) == "？" or not str(token.lemma_) == "？":
          continue
      exclusioned_text.append(str(token.lemma_))
  return exclusioned_text

def get_vector(text):
  count_vect = TfidfVectorizer(analyzer=split_words)
  Tfidf = count_vect.fit_transform(text)
  X = Tfidf.todense()
  return [X,count_vect]

def data_check(text):
  data = split_words(text)
  if len(data) <= 3:
    return False
  return True

def formatter(data,target):
  tmp = []
  lables = []
  global bar
  for i in range(len(data)):
    bar.update(1)
    if data[i][0] == "プロローグ":
      continue
    if data_check(data[i][3]) == False:
      continue
    if i == 0:
      continue
    if data[i][target] == '':
      if i%3 == 0:
        lables.append(13)
      else:
        continue
    else:
      try:
        key = [k for k, v in TAG.items() if v == data[i][target]][0]
      except:
        continue
      if key == None:
        lables.append(13)
      else:
        lables.append(int(key))
    tmp.append(data[i][3])
  return [tmp,lables]

def chek_os_path(file):
  data_dmp_win = "dmp/parser/data/"+str(re.sub(r'\.csv','',str(re.sub(r"data\\",'',str(file)))))+'.dmp'
  label_dmp_win = "dmp/parser/label/"+str(re.sub(r'\.csv','',str(re.sub(r"data\\",'',str(file)))))+'.dmp'
  data_dmp_linux = "dmp/parser/data/"+str(re.sub(r'\.csv','',str(re.sub(r"data/",'',str(file)))))+'.dmp'
  label_dmp_linux = "dmp/parser/label/"+str(re.sub(r'\.csv','',str(re.sub(r"data/",'',str(file)))))+'.dmp'
  if os.name == "nt":
    return [data_dmp_win ,label_dmp_win]
  elif os.name == "posix":
    return [data_dmp_linux,label_dmp_linux]

def data_input(file,now,total):
  global bar
  dmp_data_path,dmp_label_path = chek_os_path(file)
  if os.path.exists(dmp_data_path):# and os.path.exists(label_dmp):
    with open(dmp_data_path,'rb') as f_data:
      data = pickle.load(f_data)
    with open(dmp_label_path,'rb') as f_label:
      label = pickle.load(f_label)
    bar = tqdm(total = len(data))
    bar.set_description("Input File : ["+file+'] : ' + str(now) +'/' + str(total) )
    bar.update(len(data))
    bar.close()
    return data,label
  with open(file,encoding='utf-8') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
  target = TRAGET["param1"]
  bar = tqdm(total = len(data))
  bar.set_description("Input File : ["+file+'] : ' + str(now) +'/' + str(total) )
  data,label = formatter(data,int(target))
  with open(dmp_data_path, 'wb') as f_data:
    pickle.dump(data,f_data)
  with open(dmp_label_path, 'wb') as f_label:
    pickle.dump(label,f_label)
  bar.close()
  return [data,label]

def result(model,x,y):
  plt.title("Loss Curve")
  plt.plot(model.loss_curve_)
  plt.xlabel("Iteration")
  plt.ylabel("Loss")
  plt.grid()
  plt.show()
  print(model.score(x,y))

def mlp(X,Y):
  model = MLPClassifier(max_iter=1876,verbose=True,alpha=0.003732,validation_fraction=0.6456,hidden_layer_sizes=(100,),tol=0.0016244,solver='sgd',learning_rate_init=0.0023063,learning_rate='adaptive')
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)
  model.fit(X_train,Y_train)
  result(model,X_test,Y_test)
  return model

def search_param_mlp(trial):
  tmp=0
  global X
  global Y
  for i in range(2):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)
    param = {
      'max_iter' : trial.suggest_int('max_iter',1000,10000),
      'alpha' : trial.suggest_uniform('alpha',0.0001,0.01),
      'validation_fraction' : trial.suggest_uniform('validation_fraction',0.0,1.0),
      'hidden_layer_sizes' : [100],
      'tol' : trial.suggest_loguniform('tol',1e-7,1e-2),
      'learning_rate_init' : trial.suggest_uniform('learning_rate_init',0.0001,0.01),
      'solver' : 'sgd',
      'learning_rate' : 'adaptive',
    }
    model = MLPClassifier(**param)
    model.fit(X_train,Y_train)
    tmp+=model.score(X_test,Y_test)
  print(["+Result:"+str(tmp/2)])
  return 1-tmp/2
  
def search_param(x,y):
  global X
  X = x
  global Y
  Y = y
  study = optuna.create_study()
  study.optimize(search_param_mlp,n_trials=10)
  print(study.best_value)
  print(study.best_params)
  return study.best_params

def main():
  global bar
  file_list = glob.glob(r"data/*.csv")
  learn_data = []
  label_list = []
  i = 0
  print("[+]Input File")
  for file in file_list:
    i+=1
    data, label = data_input(file,i,len(file_list))
    learn_data.extend(data)
    label_list.extend(label)
  print("[+]TF-IDF")
  if os.path.exists("sample.dmp"):
    if 'y' == 'y':
      with open("sample.dmp",'rb') as f:
        x = pickle.load(f)
        vectorizer = TfidfVectorizer(analyzer=split_words)
    else:
      bar = tqdm(total = len(learn_data))
      bar.set_description('TF-IDF')
      x, vectorizer = get_vector(learn_data)
      with open("sample.dmp", 'wb') as f:
        pickle.dump(x,f)
      bar.close()
  else:
    bar = tqdm(total = len(learn_data))
    bar.set_description('TF-IDF')
    x, vectorizer = get_vector(learn_data)
    with open("sample.dmp", 'wb') as f:
      pickle.dump(x,f)
    bar.close()
  y = label_list
  print("[+]MLP")
  #search_param(x,y)
  model = mlp(x,y)
  os.remove("model/cl_basic.pkl.cmp")
  os.remove("vectorizer/cl_basic.pkl.cmp")
  joblib.dump(model,"model/cl_basic.pkl.cmp",compress=True)
  print("[+]Save model")
  joblib.dump(vectorizer,"vectorizer/cl_basic.pkl.cmp",compress=True)
  print("[+]Save vectorizer")
  print("[+]All process success!!")


if __name__ == "__main__":
  main()