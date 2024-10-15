from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

class YandexAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.yandex.com/"

    def get_answer(self, query):
        """Запрос к Яндекс API и получение ответа."""
        url = f"{self.base_url}/search"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        params = {
            "query": query
        }
        
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}

yandex_api = YandexAPI("https://api.yandex.com/3dacb82c-b99a-49c0-ae15-ee9c9313a5cf")

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query')
    result = yandex_api.get_answer(query)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)