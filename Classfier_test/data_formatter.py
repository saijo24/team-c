import csv
import glob
from time import sleep
import spacy
from pprint import pprint
import re

def main():
    data_in_dir = ["villager_win","wolf_win"]
    nlp = spacy.load('ja_ginza')
    for i in range(len(data_in_dir)):
        file_list = glob.glob(data_in_dir[i]+"/*")
        for file in file_list:
            out_data = []
            with open(file,encoding="utf-8_sig") as f:
                print(file)
                reader = csv.reader(f)
                data_list = [row for row in reader]
            for j in range(len(data_list)):
                try:
                    doc = nlp(data_list[j][3])
                except:
                    continue
                for sent in doc.sents:
                    tmp = [data_list[j][0],data_list[j][1],data_list[j][2]]
                    if re.match(r'■[0-9]\.',str(sent)) or re.match(r'□[0-9]\.',str(sent)):
                        continue
                    sent=''.join(str(sent))
                    sent=re.sub(r'■[0-9]\.','',str(sent))
                    sent=re.sub(r'□[0-9]\.','',str(sent))
                    tmp.append(sent)
                    out_data.append(tmp)
            with open("out\\"+file,'w',encoding='UTF-8',newline="") as f:
                writer = csv.writer(f)
                writer.writerows(out_data)
if __name__ == "__main__":
    main()