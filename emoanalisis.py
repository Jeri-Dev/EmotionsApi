import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Datos de entrenamiento
data = pd.read_csv('training.csv')

# Separar comentarios y etiquetas de sentimiento
comments = data['text'].values
labels = data['label'].values

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
    predicted_scores = clf.predict_proba(text_vectorized)[0]
    predicted_class = clf.predict(text_vectorized)[0]
    
    sentiment_labels = ["Sad", "Happy", "Very Happy", "Angry", "Fear", "Confused"]
    predicted_sentiment = sentiment_labels[predicted_class]
    
    higher_score = round(np.max(predicted_scores) * 100, 1)

    return predicted_sentiment, higher_score



print(predict_sentiment("I'm devastated by the news of her passing. She was such a bright light in our lives and will be deeply missed."))