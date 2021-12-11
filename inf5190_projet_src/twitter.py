import tweepy

access_token = "1461848113031917573-a05i2nmhrIUY0ex8qA9zoXDmQnkFIC"
access_token_secret = "z4X5Zc3kKnoAPvI4eWSfPYLGBLkOTOSrZAHoiVFqa83WB"
API_key = "VOYGwLipTfsUvwz9lhqsMjF1U"
API_secret_key = "xafMsyPT6BS1WJEb6C8RfcNnr59UiPaqjc1yvhmq6ygD1YAVpC"

def OAuth():
    try:
        auth = tweepy.OAuthHandler(API_key, API_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        
        return auth
    
    except Exception as e:
        return None

def send_tweet():
    oauth = OAuth()
    api = tweepy.API(oauth)

    api.update_status("Tweet posté pour la démo d'INF5190")

    print('Tweet posté')