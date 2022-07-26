from cProfile import run
import json
import csv
from transformers import pipeline

def import_tweets(file):
    with open(file, encoding="utf_8") as data_file:    
        data = json.load(data_file)
    return data

def get_sentiment_analysis(json_tweets):
    data = import_tweets(json_tweets)
    csv_filename = json_tweets[:-4] + "csv"
    print(csv_filename)

    # inicializando o modelo de analise
    model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
    sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

    with open(csv_filename, 'w', newline='') as results:
        writer = csv.writer(results)
        writer.writerow(["tweet_id", "label", "score"])

        for tweet in data['data']:
            # print(tweet['text'])
            # print(sentiment_task(tweet['text'])[0]['label'])
            # print(sentiment_task(tweet['text'])[0]['score'])

            row = [tweet['id'], sentiment_task(tweet['text'])[0]['label'], sentiment_task(tweet['text'])[0]['score']]
            writer.writerow(row)

def run_analysis():
    get_sentiment_analysis("tweets/aprendizado_maquina.json")
    get_sentiment_analysis("tweets/carro_autonomo.json")
    get_sentiment_analysis("tweets/chatbot.json")
    get_sentiment_analysis("tweets/dalle.json")
    get_sentiment_analysis("tweets/inteligencia_artificial.json")

run_analysis()