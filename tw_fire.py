import twitter
import sys
def oauth_login():
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information
    # on Twitter's OAuth implementation.

    CONSUMER_KEY = 'mhF9p0bY1rj3S5YTtkIIoBNEx'
    CONSUMER_SECRET = 'YxZGFGIbKLQ5TdzgMTbu7JjYkATCiyrvYQ4EtTO8GDrw5cNRd3'
    OAUTH_TOKEN = '2492696552-qplePWNJQ7tERmhU8SbzUFyEbACV5hZRmRBrt2M'
    OAUTH_TOKEN_SECRET = 'FwOmtWJS6xxa2w0uuhlob9OjKjgczq38E5sQKIC8QWkha'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    return twitter_api

# Query terms
q = 'Modi' # Comma-separated list of terms

print ('Filtering the public timeline for track=',q,file=sys.stderr)

# Returns an instance of twitter.Twitter
twitter_api = oauth_login()

# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

# See https://dev.twitter.com/docs/streaming-apis
stream = twitter_stream.statuses.filter(track=q)

# For illustrative purposes, when all else fails, search for Justin Bieber
# and something is sure to turn up (at least, on Twitter)

for tweet in stream:
    print (tweet['text'])
