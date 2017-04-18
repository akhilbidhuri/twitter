import json
import twitter

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

def twitter_trends(twitter_api, woe_id):
    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a special-case keyword argument.
    return twitter_api.trends.place(_id=woe_id)

# Sample usage

twitter_api = oauth_login()

# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/ for details on
# Yahoo! Where On Earth ID

WORLD_WOE_ID = 23424848
world_trends = twitter_trends(twitter_api, WORLD_WOE_ID)
res=json.dumps(world_trends, indent=1)
print (res)

#US_WOE_ID = 23424977
#us_trends = twitter_trends(twitter_api, US_WOE_ID)
#print (json.dumps(us_trends, indent=1))
