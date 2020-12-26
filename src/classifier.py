import collections, string, os
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

TRAIN_RATIO = 0.8

class Classifier:
    def __init__(self, parsed_dir):
        self.parsed_dir = parsed_dir

    def classify_pdfs(self):
        train_words = []
        test_words = []

        files =  os.listdir(self.parsed_dir)
        train_index = round(TRAIN_RATIO * len(files))
        
        train_files = files[:train_index]
        test_files = files[train_index:]

        for filename in train_files:
            self.add_file_to_word_bag(filename, train_words)
            
        for filename in test_files:
            self.add_file_to_word_bag(filename, test_words)
           
        vectorizer = TfidfVectorizer()
        vectorizer.fit_transform(train_words)

        results = vectorizer.transform(test_words)
        print(vectorizer.get_feature_names())

    def add_file_to_word_bag(self, filename, bag):
        f = open(self.parsed_dir + filename, 'r')
        text = f.read()
        words = self.get_words(text)
        bag.append(words)
        f.close()

    def get_words(self, text):
        no_punc = [ str.lower(w) for w in text.split() if w not in string.punctuation ]
        return ' '.join(no_punc)

    def tf_idf(self, document):
        tf = self.term_frequency(document)
        # idf = inverse_document_frequency(document)

    def term_frequency(self, document):
        counts = collections.defaultdict(int)

        doc = document.split()
        doc_length = len(doc)
        words = set(doc)

        no_punc = [''.join(c for c in s if c not in string.punctuation) for s in doc]
        
        for word in no_punc:
            counts[word] += 1

        return counts

    


