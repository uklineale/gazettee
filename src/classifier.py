import collections, string


class Classifier:
    def __init__(self, polished_docs_dir, train_range, test_range):
        self.docs_dir = polished_docs_dir
        self.train_start = train_range[0]
        self.train_end = train_range[1]
        self.test_start = test_range[0]
        self.test_end = test_range[1]

    def classify_pdfs(self):
        for filename in os.listdir(self.parsed_dir):
            print("Classifying " + filename)
            
            vectorizer = TfidfVectorizer()
            vectorizer.fit_transform(train_set)

            print(vectorizer.get_feature_names())

    def tf_idf(self, document):
        tf = term_frequency(document)
        idf = inverse_document_frequency(document)

    def term_frequency(self, document):
        counts = collections.defaultdict(int)

        doc = document.split()
        doc_length = len(doc)
        words = set(doc)

        no_punc = [''.join(c for c in s if c not in string.punctuation) for s in doc]
        
        for word in no_punc:
            counts[word] += 1

        return counts

    


