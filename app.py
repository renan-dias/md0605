from flask import Flask, request, jsonify, render_template
from modelo import BotIA

bot = BotIA()
bot.carregar()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/responder", methods=["POST"])
def responder():
    msg = request.json["mensagem"]
    resposta = bot.responder(msg)
    return jsonify({"resposta": resposta})

@app.route("/ensinar", methods=["POST"])
def ensinar():
    dados = request.json
    bot.frases.append(dados["pergunta"])
    bot.respostas.append(dados["resposta"])
    bot.treinar([{"pergunta": p, "resposta": r} for p, r in zip(bot.frases, bot.respostas)])
    bot.salvar()
    return jsonify({"resposta": "Aprendi! Obrigado por ensinar."})

if __name__ == "__main__":
    app.run(debug=True)
