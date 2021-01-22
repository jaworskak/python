#  zeby polaczyc sie z api facebooka trzeba wejśc na https://developers.facebook.com/, zarejestrować się, dodać nową aplikację, wejść w tools> graph api explorer
#  wtedy mozna wygenerować sobie token
#  potem sciagam https://facebook-sdk.readthedocs.io/en/latest/install.html czyli komenda: pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk

from  facebook import GraphAPI
import json

def read_creds(filename):
    with open(filename) as f:
        credentials = json.load(f)
    return credentials


credentials = read_creds('credentials.json')

graph = GraphAPI(access_token=credentials['access_token'])

