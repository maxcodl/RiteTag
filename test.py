from ritetag import RiteTagApi
from nltk.tokenize import word_tokenize

access_token = '2fe342b61da1aacf32d3429496c82a8bb968267277c1'
client = RiteTagApi(access_token)

def limit_80_percentage_reached(limit):
    message = 'Used {}% of API credits. The limit resets on {}'.format(limit.usage, limit.reset)
    print(message)

client.on_limit(80, limit_80_percentage_reached)

text = "The turmoil from China's strict anti-Covid measures is reaching factory floors. Automakers in China including Volkswagen and Honda have halted production at some plants, as the impact of the country's Covid restrictions rolls across a wider swath of the industrial sector. (WSJ)"

hashtags = client.hashtag_suggestion_for_text(text)
for hashtag in hashtags:
    print('Hashtag: #{}'.format(hashtag.hashtag))
    print('Exposure: {}%'.format(hashtag.exposure))
    print('Tweets per hour: {}'.format(hashtag.tweets))
    print('\n')
 