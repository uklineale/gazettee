import boto3
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Consume from SQS 
train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.", "We can see the shining sun, the bright sun.")

# Why does this have stopword features? 
# I thought tf-idf used log(idf) to scale out frequent terms.
# Any log is for comparing things orders of magnitude differently.
# So do stopwords occur orders of magnitude larger than meaningful words? Huh, language is clumsy
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(train_set)

print(vectorizer.get_feature_names())
