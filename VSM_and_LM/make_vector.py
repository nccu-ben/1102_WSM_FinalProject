import csv

# with open('./dressipi_recsys2022/train_sessions.csv', newline='') as csvfile:
#     sessionDocuments = list(csv.reader(csvfile))
#     sessionDocuments = sessionDocuments[2:]

with open('./dressipi_recsys2022/item_features.csv', newline='') as csvfile2:
    features = list(csv.reader(csvfile2))
    features = features[1:]

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
for i in range(0,len(features)):
    if(i>0):
        if(features[i][0]!=features[i-1][0]):          
            item_feature_start[features[i][0]]=i        #如果和上一列的item不一樣，紀錄這格為這個item的起點
            item_feature_end[features[i-1][0]]=i-1      #如果和上一列的item不一樣，紀錄這格為上一個item的終點
item_feature_end[features[len(features)-1][0]]=len(features)-1     #最後一個item的終點


##########################對每一列features去看有沒有這個組合 所以假如同樣itemID是2他會有很多列vectors 而這些vectors都只有一個1跟很多個0
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
    vectors.append(vector_line)
    vector_line=[]

##########################把屬於同一個itemID的vectors合併起來 放到finalvector這個dict裡 key是itemID value是他的vector
finalvector=dict()
finalvector_line=[]
ii=0    #這個變數會在features跳著走 會跳過同樣的itemID 才不會重複計算到
for k in range(0,len(item_feature_start)):
    # finalvector_line.append(features[i][0])
    for j in range(item_feature_start[features[ii][0]],item_feature_end[features[ii][0]]+1): 
        if(j == item_feature_start[features[ii][0]]):
            finalvector_line=vectors[j]
        else:
            for k in range(0,len(vectors[j])):
                finalvector_line[k]=finalvector_line[k]+vectors[j][k]
    
    finalvector[features[ii][0]]=finalvector_line
    finalvector_line=[]
    ii=item_feature_end[features[ii][0]]+1
