import pickle
import sklearn
import pandas as pd

def load_logistics_vectorizer():
    model_dir = 'trained_models/'
    vec_file = model_dir + 'vectorizer-logistics.pickle'
    load_vect = pickle.load(open(vec_file, 'rb'))
    return load_vect


def load_logistics_model():
    model_dir = 'trained_models/'
    file_name = model_dir + 'final_logistics_regression.sav'
    loaded_model = pickle.load(open(file_name, 'rb'))
    return loaded_model

def analyze_tweet_sentiment(tweets):
    df = pd.DataFrame()
    vect = load_logistics_vectorizer()
    logistics_model = load_logistics_model()
    tweet_vectorized = vect.transform(tweets)
    df["predictions"] = logistics_model.predict(tweet_vectorized)
    df["predictions"] = df["predictions"].replace({0:'Negative'})
    df["predictions"] = df["predictions"].replace({1:'Positive'})
    return df["predictions"]



if __name__ =='__main__':
    load_logistics_vectorizer()
    load_logistics_model()

