from django.db import models

# Create your models here.



import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def call_model(text):

    try:

        # modeli yukleme
        train = pd.read_csv('C:/Users/Evrim/PycharmProjects/sentimentAnalysis/static/train.tsv', sep='\t', lineterminator='\r')
        y_train=train['Etiket']
        raw_text=train['Yorum']
        le = LabelEncoder()
        le.fit(y_train)
        model_path = "C:/Users/Evrim/PycharmProjects/sentimentAnalysis/static/model.pkl"
        loaded_model = pickle.load(open(model_path, 'rb'))
        vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        X_ngrams = vectorizer.fit_transform(raw_text)

        res = loaded_model.predict(vectorizer.transform([(text)]))
        sonuc = le.inverse_transform(res)

        # 1 olumlu
        # 2 olumsuz
        # 0 notr

        return  sonuc

    except ValueError:
        print("Lütfen yazım kurallarına uygun cümle  giriniz.")
        log_file = open("log.txt", "w")
        log_file.write()
        log_file.close()

    except ConnectionError:
        print('Servis bağlantısında bir hata oluştu..')
        log_file = open("log.txt", "w")
        log_file.write()
        log_file.close()
