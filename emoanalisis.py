import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Datos de entrenamiento
data = pd.read_csv('data.csv')

# Separar comentarios y etiquetas de sentimiento
comments = data['Tweets'].values
labels = data['Feeling'].values

# Preprocesamiento de datos
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(comments)
y = np.array(labels)

# Entrenamiento del modelo
clf = MultinomialNB()
clf.fit(X, y)

# Función para predecir el sentimiento de un texto dado
def predict_sentiment(text):
    text_vectorized = vectorizer.transform([text])
    predicted_sentiment = clf.predict(text_vectorized)
    return predicted_sentiment[0]



