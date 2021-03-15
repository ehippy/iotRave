import tweepy
import secrets

# create a secrets.py file containing the following vars
# tw_consumer_key, tw_consumer_secret, tw_access_token, tw_access_secret

auth = tweepy.OAuthHandler(secrets.tw_consumer_key, secrets.tw_consumer_secret)
auth.set_access_token(secrets.tw_access_token, secrets.tw_access_secret)

api = tweepy.API(auth)

colors_we_like = ['red', 'blue', 'green', 'yellow', 'pink', 'cyan', 'magenta', 'orange', 'pink']

colors_filter = " OR ".join(colors_we_like)

search_result = api.search(
    q="love (" + colors_filter + ") -follow -hate -filter:links -filter:replies -RT",
    result_type='recent', count=20)

for tweet in search_result:
    tweet_words = tweet.text.split(' ')

    found_color = None
    for color in colors_we_like:
        for word in tweet_words:
            if color == word.lower():
                found_color = color
                break

    if found_color:
        outgoing_tweet = "#Cheerlights 💕 @{user_name} because they 💖 {color}"\
            .format(user_name=tweet.author.screen_name, color=found_color)
        api.update_status(outgoing_tweet, in_reply_to_status_id=tweet.id)
        api.create_favorite(tweet.id)
        print("Tweeted:" + outgoing_tweet)
        break

print("done")
