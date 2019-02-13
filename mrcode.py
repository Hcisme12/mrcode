import random
import sched, time
import datetime
from time import gmtime, strftime, sleep
import tweepy
schedule = sched.scheduler(time.time, time.sleep)

# j is time in seconds
# 900s == 15 mins
j = 15
sec = j


def Botman():
    a = "Null"
    adj = pickAdj()
    string = [f"{adj} facts",
    f"die for the C0d3",
    f"69",
    f"PK C0DE",
    f"{adj} facts",
    f" @smoothboy4431 is a great man",
    f"Sm3lly T00t",
    f"!!",
    f"{adj} facts",
    f"{adj} facts",
    f"Pyth0n is life",
    f"{adj} factoids",
    f"take a p00p for tha iphonr 8",
    f"Donald Trump phone number = (773) 202 - DUMP ... #DonaldTrumpPhoneNumber ",
    f"{adj} facts",
    f"What did the fat computer nerd do 4 lunch?     'Coded a damn Bigmac, mcgangbang, and a number 4'",
    f"bleep boop click click click",
    f"click cl1ck b00p",
    f"{adj} factorious truthalumous",
    f" 'Error: line 52, 59, 21, 35 and 64'",
    f"ZZZZzzzzz says the sleepy hacker.. zZZzz",
    f"{adj} facts",
    f"{adj} truth",
    f"{adj} facts",
    f"How many lines of c0de does it take to speak spanish?    'Like juan or 2'",
    f"{adj} facts"]
    
    return random.choice(string)

#This is Fact Bot

def pickAdj():
    string = [f"Massive",
    f"Major",
    f"Insanely",
    f"Big",
    f"Fun",
    f"Galactic",
    f"Gorilla Sized",
    f"Bafoon Sized",
    f"Retr0",
    f"Fugging Huge",
    f"Tiny",
    f"Largo",
    f"208 coming 4 u",
    f"Richter and Simon",
    f"depressing",
    f"Lucky",
    f"buffalo",
    f"Mr. C0de speaks only",
    f"Marc",
    f"big boy",
    f"light speed",
    f"Micro"]

    return random.choice(string)



def phrase_start():
    tweetOut = "Null" 
    tweetOut = Botman()

    return tweetOut



def main(sc):
    sec = j
    phrase_final = phrase_start()
    argfile = "twitterlog.txt"

    #defines twitter authentication keys and tweepy API
    #these have been censored for the sake of privacy
    
    cachedTweet = open(argfile, 'w')
    cachedTweet.write(phrase_final)
    cachedTweet.close()

    consumer_key = 'TnWIVggPVJ0YvnBH1Ds5SYByI'
    consumer_secret  = 'm2sl3ZosEtKDYNV0fsEsqaGDWVedxlTOM77xBBdMsKINFMDvJx'
    access_key = '866974093-at8eEI3eTP1T68dpk0LvzLu1dTVbRICL8ZJnwshn'
    access_secret = 'aw5RI8KQ4WZZalvCQ0LAzMEpTbCLazaXY8H0kzf1TFfGj'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    cachedTweet = open(argfile, 'r')
    f = cachedTweet.readlines()
    cachedTweet.close()

    #capture tweet time datetimeVar = str(datetime.datetime.now())

    for line in f:
        try:
            api.update_status(line)
        except tweepy.error.TweepError:
            print("Error: tweet not posted...")
            print("Was there a duplicate tweet?")
    schedule.enter(sec,1,main,(sc,))
schedule.enter(sec,1,main,(schedule,))
schedule.run()