from datetime import datetime
import json
from kafka import KafkaConsumer
from json import loads
from random import randint

from analyzer import Analyzer
from tweet import Tweet

consumer = KafkaConsumer(
    'kafka-tweets',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=randint(100000,100000000),
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    consumer_timeout_ms=1000)
tweets = []
m = ""
for message in consumer:
    m += message.value["message"]
    tweets.append(Tweet(message.value["name"],message.value["message"],datetime.strptime(message.value["date"], "%m/%d/%Y, %H:%M:%S")))
data = {}
data.update({"First":Analyzer.get_user_list(tweets)})
data.update({"Second": Analyzer.second_analysis(tweets)})
data.update({"Third":Analyzer.third_analysis(tweets, 4)})
data.update({"Forth": Analyzer.forth_analysis(tweets, 4)})
data.update({"Fifth": Analyzer.fifth_analysis(m)})
with open('data.json', 'w') as f:
    json.dump(data, f)


