import spotipy.util as util

username = 'gavee_123'
client_id ='5c87be52b8f94391993c896f21798ef4'
client_secret = '453f165af7104da1a51e730608c5fd03'
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)
