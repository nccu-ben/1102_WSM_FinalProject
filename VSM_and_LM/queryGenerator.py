import csv
from time import sleep
from tqdm import tqdm, trange

with open('./dressipi_recsys2022/test_leaderboard_sessions.csv', newline='') as csvfile:

    sessionDocuments = list(csv.reader(csvfile))
    sessionDocuments = sessionDocuments[1:]
    
    nowSessionId = -1
    path = ""

    for i in tqdm(sessionDocuments):
        if i[0] != nowSessionId:
            nowSessionId = i[0]
            if path != "":
                f.close()

            path = './queries/' + nowSessionId + '.txt'
            f = open(path, 'w')
        
        f.write(i[1])
        f.write(" ")
        f.write(i[2][0:7])
        f.write(" ")
