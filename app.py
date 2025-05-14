from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Usa tu propia clave de API de OpenAI si quieres desplegarlo tú
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "No te entendí, ¿puedes repetir?"})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": "Hubo un error. Intenta más tarde."})

if __name__ == "__main__":
    app.run(debug=True)
