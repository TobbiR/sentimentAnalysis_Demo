from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import configparser


cfg = configparser.ConfigParser()
cfg.read('twitterAnalysis.cfg')

#Variables that contain the user credentials to access Twitter API
access_token = cfg.get('access_token','access_token')
access_token_secret = cfg.get('access_token','access_token_secret')
consumer_key = cfg.get('consumer','consumer_key')
consumer_secret = cfg.get('consumer','consumer_secret')


#listener - receives tweets from stdout
class StdOutListener(StreamListener):

    def on_data(self, data):
        if len(data) > 1:

            data = json.loads(data)
            crdt = data['created_at']
            id = data['id_str']
            text = data['text']
            text = str(text).replace("'", "''")
            lang = data['lang']
            if data['place'] != None:
                loc = data['place']['country']
            else:
                loc = 'None'
            if 'retweeted_status' in data:
                rt = True
            else:
                rt = False

            print(rt, crdt, id, text, lang, loc)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#nfl'])