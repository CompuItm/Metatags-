from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configura tu API Key de OpenAI
openai.api_key = ''

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para interactuar con ChatGPT
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    try:
        # Llamada a la API de OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # O el modelo que prefieras
            prompt=user_message,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        chatgpt_response = response.choices[0].text.strip()

        return jsonify({'response': chatgpt_response})

    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
