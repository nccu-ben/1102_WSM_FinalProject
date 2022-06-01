import csv
import numpy as np

# with open('./dressipi_recsys2022/train_sessions.csv', newline='') as csvfile:
#     sessionDocuments = list(csv.reader(csvfile))
#     sessionDocuments = sessionDocuments[2:]

with open('./dressipi_recsys2022/item_features.csv', newline='') as csvfile2:
    features = list(csv.reader(csvfile2))
    features = features[1:471752]
############################所有組合可能
allcombination=[]
combination=[]
for i in range(1,74):
    for j in range(1,906):
        combination.append(str(i))
        combination.append(str(j))
        allcombination.append(combination)
        combination=[]

###################讓同樣的item易於計算
item_feature_start=dict()     #記錄這個item他從item_feature這個檔案的第幾列開始(since item_feature is sorted)
item_feature_end=dict()       #記錄這個item他從item_feature這個檔案的第幾列結束(since item_feature is sorted)

item_feature_start['2']=0     #初始化第一格
head=[]  #紀錄個別items
head.append('2')
for i in range(0,len(features)):
    if(i>0):
        if(features[i][0]!=features[i-1][0]):          
            item_feature_start[features[i][0]]=i        #如果和上一列的item不一樣，紀錄這格為這個item的起點
            item_feature_end[features[i-1][0]]=i-1      #如果和上一列的item不一樣，紀錄這格為上一個item的終點
            head.append(features[i][0])
item_feature_end[features[len(features)-1][0]]=len(features)-1     #最後一個item的終點



##########################對每一列features去看有沒有這個組合
allitem=dict()   #key是item value是vector
init=[]
for i in range(0,len(allcombination)):
    init = init + [0]
for i in range(0,len(head)):
    allitem[head[i]]=init
vector_line=[]
vectors=[]
for i in range(0,len(features)):
    # for j in range(item_feature_start[features[i][0]],item_feature_end[features[i][0]]+1): 
    # vector_line.append(features[i][0])
    for k in range(0,len(allcombination)):  
        if(features[i][1]==allcombination[k][0] and features[i][2]==allcombination[k][1]):
            vector_line.append(1)
        else:
            vector_line.append(0)
    allitem[features[i][0]]=np.sum([vector_line,allitem[features[i][0]]],axis=0)
    # vectors.append(vector_line)
    vector_line=[]

path = 'finalvectors.txt'
f = open(path, 'w')
for i in range(0,len(allitem)):
    print((head[i],allitem[head[i]].tolist()), file=f)
f.close()

