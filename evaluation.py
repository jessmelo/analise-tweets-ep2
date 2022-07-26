def import_labeled(file):
    with open(file, encoding="utf_8") as data_file:    
        data = json.load(data_file)
    return data

def create_test_txt(file):
    data = import_labeled(file)
    neutral = 0
    positive = 0
    negative = 0
    tweets = 0
    test_labels = "test_labels.csv"

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

    with open(csv_filename, 'w', newline='') as results:
        import csv
        writer = csv.writer(results)
        writer.writerow(["tweet_id", "label", "score"])

        writer = csv.writer(results)
        writer.writerow(["tweet_id", "label", "score"])

        for tweet in data['data']:
            # print(tweet['text'])
            # print(sentiment_task(tweet['text'])[0]['label'])
            # print(sentiment_task(tweet['text'])[0]['score'])

            row = [tweet['id']
            writer.writerow(row)

