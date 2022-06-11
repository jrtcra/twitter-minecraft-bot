import tweepy
import keys
import random


client = tweepy.Client(keys.bearer_token, keys.api_key, keys.key_secret, keys.access_token, keys.access_token_secret)

auth = tweepy.OAuth1UserHandler(keys.api_key, keys.key_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

testarray = ["https://minecraft.fandom.com/wiki/Trading", "https://minecraft.fandom.com/wiki/Brewing", "https://minecraft.fandom.com/wiki/Enchanting", "https://minecraft.fandom.com/wiki/Mob", "https://minecraft.fandom.com/wiki/Block", "https://minecraft.fandom.com/wiki/Item", "https://minecraft.fandom.com/wiki/Crafting", "https://minecraft.fandom.com/wiki/Smelting", "https://minecraft.fandom.com/wiki/Tutorials", "https://minecraft.fandom.com/wiki/Resource_Pack", "https://minecraft.fandom.com/wiki/Redstone_circuits"]
tweetlist = random.choice(testarray)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=tweetlist)

stream = MyStream(bearer_token=keys.bearer_token)

rule = tweepy.StreamRule("(#ChunkBot) (-is:retweet -is:reply)")
stream.add_rules(rule)
stream.filter()

