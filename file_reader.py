import csv

from tweet import Tweet


class FileReader:
    def __init__(self):
        self.tweets = []

    def readCSV(self):
        with open('all_tweets.csv', 'r') as file:
            try:
                reader = csv.reader(file)
                for row in reader:
                    tweet = Tweet(row[4],row[5])
                    self.tweets.append(tweet)
            except UnicodeDecodeError:
                pass

