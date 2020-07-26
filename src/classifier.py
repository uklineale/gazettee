
def Classifier:
    def __init__(self, polished_docs_dir, train_range, test_range):
        self.docs_dir = polished_docs_dir
        self.train_start = train_range[0]
        self.train_end = train_range[1]
        self.test_start = test_range[0]
        self.test_end = test_range[1]

    # TODO Reaaaally need a datalake already
    def classify_pdfs(self):
        for filename in os.listdir(self.parsed_dir):
            print("Classifying " + filename)
            
            vectorizer = TfidfVectorizer()
            vectorizer.fit_transform(train_set)

            print(vectorizer.get_feature_names())