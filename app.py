from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Azure OpenAI API endpoint
OPENAI_API_ENDPOINT = "https://name26124.openai.azure.com/openai/deployments/gptQ1-66/completions?api-version=2023-05-15"
OPENAI_API_KEY = "c1ddbfdf45b640e0ad34c7d14d9d129b"

@app.route('/api/messages', methods=['POST'])
def messages():
    # Получаем сообщение от бота
    data = request.json
    user_message = data.get('text', '')

    # Запрос к Azure OpenAI
    response = requests.post(
        OPENAI_API_ENDPOINT,
        headers={
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        },
        json={
            "prompt": user_message,
            "max_tokens": 100
        }
    )

    # Получаем ответ от Azure OpenAI
    answer = response.json().get('choices', [{}])[0].get('text', '')

    # Возвращаем ответ обратно в Telegram
    return jsonify({"text": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
