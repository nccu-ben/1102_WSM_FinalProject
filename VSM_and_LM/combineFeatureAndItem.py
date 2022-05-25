###資料型態:(s t i (cvcvcv) i (cvcvcv)...)

import csv

with open('./dressipi_recsys2022/train_sessions.csv', newline='') as csvfile:
    sessionDocuments = list(csv.reader(csvfile))
    sessionDocuments = sessionDocuments[2:]

with open('./dressipi_recsys2022/item_features.csv', newline='') as csvfile2:
    features = list(csv.reader(csvfile2))
    features = features[1:]

item_feature_start=dict()     #記錄這個item他從item_feature這個檔案的第幾列開始(since item_feature is sorted)
item_feature_end=dict()       #記錄這個item他從item_feature這個檔案的第幾列結束(since item_feature is sorted)

item_feature_start['2']=0     #初始化第一格
for i in range(0,len(features)):
    if(i>0):
        if(features[i][0]!=features[i-1][0]):          
            item_feature_start[features[i][0]]=i        #如果和上一列的item不一樣，紀錄這格為這個item的起點
            item_feature_end[features[i-1][0]]=i-1      #如果和上一列的item不一樣，紀錄這格為上一個item的終點
item_feature_end[features[len(features)-1][0]]=len(features)-1     #最後一個item的終點

sessions=[]                                         #以session為單位，記錄這個session的所有item以及他們的feature
allsession=[]                                       #存放所有session
sessions.append(sessionDocuments[0][0])             #初始化session(放第一個session_ID)
sessions.append(sessionDocuments[0][2][0:10])       #初始化session(放第一個session_ID的時間)
#sessions.append('i'+sessionDocuments[0][1])         #初始化session(放第一個session_ID的item)

for i in range(item_feature_start['9655'],(item_feature_end['9655']+1)):     #初始化session(放第一個session_ID的item's features)
    sessions.append('i'+sessionDocuments[0][1]+'c'+features[i][1]+'v'+features[i][2])

for i in range(1,len(sessionDocuments)):
    if(sessionDocuments[i][0]==sessionDocuments[i-1][0]):     #如果在同一個session就繼續放items跟他們的features(since train_sessions is sorted)
        for j in range(item_feature_start[sessionDocuments[i][1]],(item_feature_end[sessionDocuments[i][1]]+1)):
            sessions.append('i'+sessionDocuments[i][1]+'c'+features[j][1]+'v'+features[j][2])
    else:
        allsession.append(sessions)    #如果跑到不同個session就把上一個session的資料存起來然後開始下一個session的存放(since train_sessions is sorted)
        sessions=[]
        sessions.append(sessionDocuments[i][0])
        sessions.append(sessionDocuments[i][2][0:10])
        for j in range(item_feature_start[sessionDocuments[i][1]],(item_feature_end[sessionDocuments[i][1]]+1)):
            sessions.append('i'+sessionDocuments[i][1]+'c'+features[j][1]+'v'+features[j][2])

allsession.append(sessions)

with open('combineFeatureAndItem.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for i in range(0,len(allsession)):
        writer.writerow(allsession[i])

