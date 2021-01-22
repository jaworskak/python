#  zeby polaczyc sie z api facebooka trzeba wejśc na https://developers.facebook.com/, zarejestrować się, dodać nową aplikację, wejść w tools> graph api explorer
#  wtedy mozna wygenerować sobie token
#  potem sciagam https://facebook-sdk.readthedocs.io/en/latest/install.html czyli komenda: pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk

import facebook

graph = facebook.GraphAPI(access_token="EAA55Esz7ABcBAOKGm3W8BkjFPK59ZAzRcCVp7HdPVXclOy5ugxkitvdCDZB7VzpUwdN7TCXK1aOOo32vVcN0DoMVbaAdbkqTDljqHRWtHxJ6C5hLFSbXny0KXWIkk0ANdJArHvilwE5wEZCYu8ZACVvcrsRbroOJxTH9ICeEq8mbOVC2oXst4METpP9DLLKnFobsECCyhwRCchKafSnqPK3D7RxSePovjMthoqSZBawZDZD", version="3.1")


