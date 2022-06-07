from base64 import b64encode
from os import environ
import requests


def load_doppler(secret, project, config):
    url = "https://api.doppler.com/v3/configs/config/secrets/download"

    params = {
        'format': 'json',
        **({'config': config} if config else {}),
        **({'project': project} if project else {}),
        'include_dynamic_secrets': False,
        'dynamic_secrets_ttl_sec': 1800,
    }

    headers = {
        "Accept": "application/json",
        "Authorization": f"Basic {b64encode(secret + ':').decode('utf-8')}"
    }

    response = requests.get(url, params=params, headers=headers)

    for key, value in response.json().items():
        environ[key] = value
