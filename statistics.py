import json

with open("tweets/aprendizado_maquina.json", encoding="utf_8") as data_file:    
    data = json.load(data_file)
    print(data['data'])
    for tweet in data['data']:
        print(tweet['text'])
        print(" ")
