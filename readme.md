# 🧠 SimSimi Clone com IA e Matemática Discreta

> Projeto educacional que une **Matemática Discreta**, **Inteligência Artificial** e **Desenvolvimento Web** usando Python, Flask e TensorFlow.

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Discrete_Mathematics.svg/1024px-Discrete_Mathematics.svg.png" width="400" alt="Matemática Discreta">
</div>

---

## 🎓 Objetivo

Criar um **clone inteligente do SimSimi** com aprendizado ativo, onde:
- O bot **aprende com o usuário**,
- O conhecimento é salvo e reutilizado,
- A interface é **web responsiva com Bootstrap**,
- Os dados são vetorizados e processados com **TensorFlow**.

---

## 🧩 Fundamentos de Matemática Discreta

Este projeto aplica conceitos fundamentais da disciplina:

| Conceito                  | Aplicação no Projeto                              |
|--------------------------|---------------------------------------------------|
| **Funções**              | `f(mensagem) = resposta` com redes neurais        |
| **Relações**             | Cada par pergunta-resposta é uma relação binária  |
| **Conjuntos**            | Vocabulário e mensagens são subconjuntos do corpus |
| **Autômatos Finitos**    | O bot opera em estados (espera > responde > aprende) |
| **Álgebra Booleana**     | Entrada vetorial binária com `CountVectorizer`   |
| **Gramática Regular**    | Frases curtas com estrutura previsível            |

---

## 🌐 Interface Responsiva

A interface web é feita com **HTML5 + Bootstrap 5**:

<div align="center">
  <img src="https://raw.githubusercontent.com/renan-dias/md0605/main/assets/interface-bot.png" width="700" alt="Interface do Bot com Bootstrap">
</div>

---

## 🚀 Demonstração (GIF)

<div align="center">
  <img src="https://media.giphy.com/media/XG9rN5WgMGbYcajTV7/giphy.gif" width="500" alt="Bot em Ação">
</div>

---

## 🛠️ Tecnologias Usadas

- [Python 3.8+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [TensorFlow (Keras)](https://www.tensorflow.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Bootstrap 5](https://getbootstrap.com/)

---

## 📥 Como Clonar e Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/renan-dias/md0605.git
cd md0605
````

### 2. Crie e Ative um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Projeto

```bash
python app.py
```

### 5. Acesse no Navegador

```
http://127.0.0.1:5000
```

---

## 💡 Como o Bot Funciona

1. O usuário digita uma mensagem.
2. O bot procura nos dados treinados.
3. Se não encontrar, solicita uma resposta e **aprende** com o usuário.
4. Os dados são vetorizados com `CountVectorizer` e usados para re-treinar a rede neural (rede MLP com Keras).
5. O conhecimento é salvo em `modelo_dados.json`.

---

## 📚 Atividades para Sala de Aula

* Desenhe o **grafo de conhecimento** (pergunta → resposta).
* Modele o bot como um **autômato finito determinístico (AFD)**.
* Simule uma **função composta** que transforma frases em vetores e respostas.
* Crie **novos conjuntos de treinamento** e analise o desempenho do bot.

---

## 📎 Licença

Este projeto é de uso educacional, mantido por [Renan Dias](https://github.com/renan-dias).
Sinta-se à vontade para usar, estudar e modificar para fins didáticos.

---

## 🙌 Agradecimentos

* Projeto inspirado no clássico [SimSimi](https://simsimi.com/)
* Código desenvolvido com foco em **ensino prático e interdisciplinar**
