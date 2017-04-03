import re
import string

def import_text(filename):
    text_in = open(filename, "r")
    return text_in.read()

def clean_text(text):
    for char in [";",",","\"","'","(",")", " - "]:
        text = text.replace(char, "")
    text = text.replace("\n"," ")
    text = text.lower()
    return text

def get_sentences(text):
    return re.split("[.?!]", text)

def list_2grams(sentence_list):
    ngrams = []
    for sentence in sentence_list:
        words = sentence.split()
        for i in range(0, len(words) - 1):
            ngrams.append([words[i], words[i+1]])
    return ngrams

raw_text = import_text(r"C:\Users\kaiwa\Google Drive\COMP 221_ Project Folder (Garrett & Kai)\Project Code\metamorphosis.txt")

sentences = get_sentences(clean_text(raw_text)[0:1000])

print(list_2grams(sentences))

