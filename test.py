import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Presidential Debate&'
       'to=2023-07-10&'
       'from=2023-06-10'
       'sortBy=popularity&'
       'apiKey=2303fa56c58d4c328ea3bfbc05cf53a2')

response = requests.get(url)

print (response.json())