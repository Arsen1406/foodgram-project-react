import json

import requests

with open('ingredients.json', 'r', encoding='utf-8') as f:
    file = json.load(f)

url = 'http://158.160.30.98/api/ingredients/'
for js in file:
    response = requests.post(url, headers=(
        {'Authorization': 'Token bbef88e93901bda42e2b0ed9207138213c959763'}
    ), json=js)
    print(response.text)
