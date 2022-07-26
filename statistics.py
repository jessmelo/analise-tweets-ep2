from unittest import result
import pandas as pd
import json

def import_results(file):
    results = pd.read_csv (file)
    return results

def import_labeled(file):
    with open(file, encoding="utf_8") as data_file:    
        data = json.load(data_file)
    return data

def get_mean_from_results(file):
    results = import_results(file)
    percent = results['label'].value_counts(normalize=True) * 100
    mean = results["score"].mean()
    print(mean)
    print(percent)

def get_stats_from_labeled(file):
    data = import_labeled(file)
    neutral = 0
    positive = 0
    negative = 0
    tweets = 0

    for tweet in data['data']:
        if(tweet['label'] == "Neutral"):
            neutral+=1
        if(tweet['label'] == "Positive"):
            positive+=1
        if(tweet['label'] == "Negative"):
            negative+=1
        tweets+=1

    print(file)
    print("Neutral " + str((neutral/tweets * 100)))
    print("Positive " + str((positive/tweets * 100)))
    print("Negative " + str((negative/tweets * 100)))

# get_mean("tweets/aprendizado_maquina.csv")
# get_mean("tweets/carro_autonomo.csv")
# get_mean("tweets/chatbot.csv")
# get_mean("tweets/dalle.csv")
# get_mean("tweets/inteligencia_artificial.csv")

get_stats_from_labeled("tweets/aprendizado_maquina_rotulado.json")
get_stats_from_labeled("tweets/carro_autonomo_rotulado.json")
get_stats_from_labeled("tweets/chatbot_rotulado.json")
get_stats_from_labeled("tweets/dalle_rotulado.json")
get_stats_from_labeled("tweets/inteligencia_artificial_rotulado.json")