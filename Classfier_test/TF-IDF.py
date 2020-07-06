import csv
import glob
from time import sleep
from pprint import pprint

TRAGET = {"param1":4,"param2":5,"param3":6}

def formatter(data,target):
    tmp = []
    lables = []
    for i in range(len(data)):
        if i == 0:
            continue
        tmp.append(data[i][3])
        if data[i][target] == '':
            lables.append('None')
        else:
            lables.append(data[i][target])
    return tmp,lables

def data_input(file):
    with open(file) as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    target = TRAGET["param1"]
    data = formatter(data,int(target))
    return data

def main():
    file_list = glob.glob(r"data/*.csv")
    for file in file_list:
        print(file)
        input_data = data_input(file)
        data = input_data[0]
        label = input_data[1]
if __name__ == "__main__":
    main()