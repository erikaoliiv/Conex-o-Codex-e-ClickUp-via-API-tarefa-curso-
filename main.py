import os

import requests
from dotenv import load_dotenv


def load_trello_credentials():
    load_dotenv()

    api_key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_TOKEN")

    if not api_key or not token:
        raise RuntimeError(
            "Configure TRELLO_API_KEY e TRELLO_TOKEN no arquivo .env antes de executar."
        )

    return api_key, token


def example_request():
    api_key, token = load_trello_credentials()

    url = "https://api.trello.com/1/members/me"
    params = {
        "key": api_key,
        "token": token,
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    user = response.json()
    print("Conexao com Trello realizada com sucesso.")
    print(f"Usuario autenticado: {user.get('fullName') or user.get('username')}")


if __name__ == "__main__":
    example_request()
