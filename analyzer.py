from collections import OrderedDict
from datetime import datetime, timedelta
import re


class Analyzer:
    @staticmethod
    def get_user_list(tweets):
        user_list = []
        for tweet in tweets:
            user_list.append(tweet.name)
        return list(set(user_list))

    @staticmethod
    def second_analysis(tweets):
        user_to_tweets = dict()
        for tweet in tweets:
            time = tweet.date
            if datetime.now() - timedelta(hours=24) <= time:
                if tweet.name not in user_to_tweets.keys():
                    user_to_tweets.update({tweet.name: [tweet.message]})
                else:
                    tmp = user_to_tweets.get(tweet.name)
                    tmp.append(tweet.message)
                    user_to_tweets.update({tweet.name: tmp})
        user_to_tweets = OrderedDict(sorted(user_to_tweets.items(), key=lambda kv: (len(kv[1]))))
        selected_users = dict()
        for i in range(10):
            user_d = user_to_tweets.popitem(last=True)
            if len(user_d[1]) > 10:
                user_d[1].reverse()
                tmp = select_most_resent_posts(user_d[1][:10])
            else:
                tmp = user_d[1:][0]
            selected_users.update({user_d[0]: tmp})
        return selected_users

    @staticmethod
    def third_analysis(tweets, hour):
        user_stats = dict()
        a = 1
        while a <= hour:
            for tweet in tweets:
                time = tweet.date
                if datetime.now() - timedelta(hours=hour) <= time:
                    if tweet.name not in user_stats.keys():
                        user_stats.update({tweet.name: [1]})
                    elif len(user_stats[tweet.name]) < a:
                        tmp = user_stats.get(tweet.name)
                        tmp.append(1)
                        user_stats.update({tweet.name: tmp})
                    else:
                        tmp = user_stats.get(tweet.name)
                        tmp[len(tmp) - 1] += 1
                        user_stats.update({tweet.name: tmp})
            a += 1
        for u_data in user_stats:
            u_d = user_stats[u_data]
            for a in range(len(u_d) - 1):
                for b in range(a + 1, len(u_d)):
                    u_d[b] -= u_d[a]
        return user_stats

    @staticmethod
    def fifth_analysis(message):
        hash_dict = dict()
        hashes = re.findall(r"#(\w+)", message)
        for h in hashes:
            if h in hash_dict.keys():
                hash_dict.update({h: hash_dict.get(h) + 1})
            else:
                hash_dict.update({h: 1})
        return hash_dict

    @staticmethod
    def forth_analysis(tweets, n):
        user_to_tweets_dict = dict()
        for tweet in tweets:
            time = tweet.date
            if datetime.now() - timedelta(hours=n) <= time:
                if tweet.name in user_to_tweets_dict.keys():
                    user_to_tweets_dict.update({tweet.name: user_to_tweets_dict.get(tweet.name) + 1})
                else:
                    user_to_tweets_dict.update({tweet.name: 1})
        u = []
        while len(u) < 20:
            u.append(get_max_key_from_dict(user_to_tweets_dict))

        return u


def get_max_key_from_dict(udict):
    max_key = max(udict, key=udict.get)
    udict.pop(max_key)
    return max_key


def select_most_resent_posts(user_d):
    user_d.reverse()
    return list(filter(lambda el: user_d.index(el) < 10, user_d))
