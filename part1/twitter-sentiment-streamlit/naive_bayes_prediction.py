import pickle
import sklearn
import pandas as pd

def load_naive_bayes_vectorizer():
    model_dir = 'trained_models/'
    vec_file = model_dir + 'vectorizer-naive_bayes.pickle'
    load_vect = pickle.load(open(vec_file, 'rb'))
    return load_vect


def load_naive_bayes_model():
    model_dir = 'trained_models/'
    file_name = model_dir + 'final_naive_bayes.sav'
    loaded_model = pickle.load(open(file_name, 'rb'))
    return loaded_model


def analyze_tweet_sentiment_with_naive_bayes(tweets):
    df = pd.DataFrame()
    vect = load_naive_bayes_vectorizer()
    naive_bayes_model = load_naive_bayes_model()
    tweet_vectorized = vect.transform(tweets)
    df["predictions"] = naive_bayes_model.predict(tweet_vectorized)
    df["predictions"] = df["predictions"].replace({0: 'Negative'})
    df["predictions"] = df["predictions"].replace({1: 'Positive'})
    return df["predictions"]


if __name__ =='__main__':
    load_naive_bayes_vectorizer()
    load_naive_bayes_model()