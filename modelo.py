import tensorflow as tf
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import json

class BotIA:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = None
        self.frases = []
        self.respostas = []

    def treinar(self, dados):
        self.frases = [d["pergunta"] for d in dados]
        self.respostas = [d["resposta"] for d in dados]

        X = self.vectorizer.fit_transform(self.frases).toarray()
        y = tf.keras.utils.to_categorical(range(len(self.respostas)))

        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(X.shape[1],)),
            tf.keras.layers.Dense(8, activation="relu"),
            tf.keras.layers.Dense(len(self.respostas), activation="softmax")
        ])

        self.model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
        self.model.fit(X, y, epochs=300, verbose=0)

    def responder(self, pergunta):
        x = self.vectorizer.transform([pergunta]).toarray()
        pred = self.model.predict(x)[0]
        index = np.argmax(pred)
        confianca = pred[index]

        if confianca > 0.6:
            return self.respostas[index]
        else:
            return "Desculpe, não entendi. Pode me ensinar?"

    def salvar(self):
        with open("modelo_dados.json", "w") as f:
            json.dump({"perguntas": self.frases, "respostas": self.respostas}, f)

    def carregar(self):
        try:
            with open("modelo_dados.json", "r") as f:
                data = json.load(f)
                self.frases = data["perguntas"]
                self.respostas = data["respostas"]
                self.treinar([{"pergunta": p, "resposta": r} for p, r in zip(self.frases, self.respostas)])
        except:
            pass
