import requests, sys, json
import string

import time



for i in range(10):
    session = requests.session()
    print ("\n\nTest " + str(i) + "\n\n")
    response = session.get('https://www.reddit.com/comments.json', headers = {'User-agent': 'COMP 221'})

    data = response.json()

    for child in data['data']['children']:
        sentence = child['data']['body']
        lowerSentence = sentence.lower()
        wordList = lowerSentence.split()
        cleanWordList = []
        for word in wordList:
            cleanWord = word.strip(string.punctuation)
            cleanWordList.append(cleanWord)
        print(cleanWordList)
    time.sleep(5)