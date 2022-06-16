from argparse import Namespace
from base64 import b64encode
from os import environ
import requests


def load_doppler(options: Namespace):
    url = "https://api.doppler.com/v3/configs/config/secrets/download"
    project = options.doppler_project
    config = options.doppler_config

    params = {
        'format': 'json',
        **({'config': config} if config else {}),
        **({'project': project} if project else {}),
        'include_dynamic_secrets': False,
        # 'dynamic_secrets_ttl_sec': 1800,
    }

    secret = options.doppler_token
    auth = b64encode(secret.encode('utf-8') + b':').decode('utf-8')

    headers = {
        "Accept": "application/json",
        "Authorization": f"Basic {auth}"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(response.text)
        exit('Bad response code from Doppler')

    j = response.json()

    options.__setattr__('doppler_env', j)

    for key, value in j.items():
        environ[key] = value
