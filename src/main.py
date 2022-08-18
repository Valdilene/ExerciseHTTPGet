import requests

# This is a HTTP Get call
response = requests.get('https://gist.githubusercontent.com/chriddyp/feaa84b34854e53fb72a/raw/dbba00aeafb981f0f50014030d1b6ad0399d957d/example-data.csv')

print(response.status_code)