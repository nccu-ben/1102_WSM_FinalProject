import csv

with open('./dressipi_recsys2022/train_sessions.csv', newline='') as csvfile:
    sessionDocuments = list(csv.reader(csvfile))
    sessionDocuments = sessionDocuments[1:]

with open('./dressipi_recsys2022/item_features.csv', newline='') as csvfile2:
    features = list(csv.reader(csvfile2))
    features = features[1:]


