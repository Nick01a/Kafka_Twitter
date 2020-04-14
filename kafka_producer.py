from time import sleep
from json import dumps
from kafka import KafkaProducer

from file_reader import FileReader

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

fileReader = FileReader()
fileReader.readCSV()
for tweet in fileReader.tweets:
    send_data = {"message": tweet.message, "name": tweet.name, "date": tweet.date.strftime("%m/%d/%Y, %H:%M:%S")}
    producer.send("kafka-tweets", value=send_data)
    sleep(0.025)
