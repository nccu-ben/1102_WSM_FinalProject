import csv
from time import sleep
from tqdm import tqdm, trange

file = open('./combineFeatureAndItem.csv','r')
    
for line in tqdm(file.readlines()):
    line = line.replace("," , " ")
    sessionId = list(line.split())[0]

    path = './documents/' + sessionId + '.txt'
    targetFile = open(path, 'w')
    targetFile.write(line)
    targetFile.close()

