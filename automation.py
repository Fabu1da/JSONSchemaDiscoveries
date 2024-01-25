import requests

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjY1YjE4NmVhZDVjZDcwOTZmYzBjNzg0YiIsInVzZXJuYW1lIjoiZmFieSIsImVtYWlsIjoiZmFieUBnbWFpbC5jb20iLCJjcmVhdGVkQXQiOiIyMDI0LTAxLTI0VDIxOjUzOjQ2LjA1OFoiLCJ1cGRhdGVkQXQiOiIyMDI0LTAxLTI0VDIxOjUzOjQ2LjA1OFoiLCJfX3YiOjB9LCJpYXQiOjE3MDYxMzMyMjZ9.gzUY0W4nENjd4z-TzPz6_yS0uInd5us-mrGfwD0kaL4"

def register(email: str, username: str, password: str) -> dict:
    json_data = {
        'email': email,
        'username': username,
        'password': password,
    }

    response = requests.post('http://localhost:3000/api/register', json=json_data)
    response.raise_for_status()
    return response.json()

def login(email: str, password: str) -> dict:

    headers = {
        #'Content-Type': 'application/json',
        'Origin': 'http://localhost:3000',
        'Referer': 'http://localhost:3000/register',
    }

    json_data = {
        'email': email,
        'password': password,
    }

    response = requests.post('http://localhost:3000/api/login', json=json_data)
    response.raise_for_status()
    return response.json()

def all(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token, 
    }

    json_data = {
        'authentication': {
            'authMechanism': 'SCRAM-SHA-1',
            'authDatabase': 'admin',
            'userName': 'mongoadmin',
            'password': 'secret',
        },
        'port': '27017',
        'address': 'mongo',
        'databaseName': 'jsonschemadiscovery',
        'collectionName': 'firenze_venues',
    }

    response = requests.post('http://localhost:3000/api/batch/rawschema/steps/all',  headers=headers, json=json_data)
    response.raise_for_status()
    return response


def view_schema(access_token):

    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    response = requests.get('http://localhost:3000/api/batch/65b18f69d095d0dce8094c18', headers=headers)
    response.raise_for_status()
    return response.json()


def view_time():
  

    headers = {
        'authority': 'translate.googleapis.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'http://localhost:3000',
        'referer': 'http://localhost:3000/',
        'x-client-data': 'CKy1yQEIi7bJAQiltskBCKmdygEItfzKAQiTocsBCN6YzQEIhqDNAQjf680BCKfuzQEIg/DNARin6s0B',
    }

    params = {
        'anno': '3',
        'client': 'te_lib',
        'format': 'html',
        'v': '1.0',
        'key': 'AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw',
        'logld': 'vTE_20240123',
        'sl': 'auto',
        'tl': 'en',
        'tc': '0',
        'tk': '217280.289669',
    }

    data = 'q=%3Ca%20i%3D0%3E%20Etapa%201%3A%20Carregar%20a%20estrutura%20dos%20registros%20(Raw%20Schema)%3A%20%3C%2Fa%3E%3Ca%20i%3D1%3E%200%3A00%3A00%3A101%20%3C%2Fa%3E&q=%3Ca%20i%3D0%3E%20Etapa%202.2%3A%20Ordenar%20alfab%C3%A9ticamente%20a%20estrutura%20dos%20documentos%20da%20etapa%202.1%20e%20reduzir%3A%20%3C%2Fa%3E%3Ca%20i%3D1%3E0%3A00%3A00%3A012%20%3C%2Fa%3E&q=%3Ca%20i%3D0%3E%20Etapa%203%3A%20Unir%20a%20estrutura%20dos%20documentos%20da%20etapa%202.2%3A%20%3C%2Fa%3E%3Ca%20i%3D1%3E%200%3A00%3A00%3A003%20%3C%2Fa%3E&q=%3Ca%20i%3D0%3E%20Etapa%204%3A%20Mapear%20estrutura%20do%20documento%20resultante%20da%20etapa%203%20para%20JSON%20Schema%3A%20%3C%2Fa%3E%3Ca%20i%3D1%3E0%3A00%3A00%3A002%20%3C%2Fa%3E&q=%3Ca%20i%3D0%3E%20Tempo%20total%3A%20%3C%2Fa%3E%3Ca%20i%3D1%3E%200%3A00%3A00%3A137%20%3C%2Fa%3E'

    response = requests.post('https://translate.googleapis.com/translate_a/t', params=params, data=data)
    response.raise_for_status()
    return response

def view_schema(access_token):


    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    response = requests.get(
        'http://localhost:3000/api/batch/jsonschema/generate/65b18f69d095d0dce8094c18',
    
        headers=headers,
    )

    response.raise_for_status()
    return response
