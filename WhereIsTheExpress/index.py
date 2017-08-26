from flask import Flask, render_template
import yaml
import requests

app = Flask(__name__)

secret = None
clint_id = None
config = {}
with open("config.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Update app config with config.yml
app.config.update(config)


def default_headers(headers=None):
    if not headers:
        headers = {}
    _default_headers = dict()
    _default_headers['Accept'] = 'application/json'
    return dict(**headers, **_default_headers)


@app.route('/')
def main():
    return render_template('index.html')


def auth():
    headers = default_headers(
        {'Content-Type': 'application/x-www-form-urlencoded '}
    )
    print(headers)
    data = {
        'client_id': app.config['auth']['client-id'],
        'client_secret': app.config['auth']['secret'],
        'grant_type': 'client_credentials',
        'scope': 'transitapi:all',
    }

    response = requests.post("https://identity.whereismytransport.com/connect/token", data=data,
                      headers=headers).json()
    return response.get('access_token')


def handle_auth(func):
    def func_wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code == 402:
            # reauthenticate
            pass
        return response
    return func_wrapper

TOKEN = auth()

if __name__ == "__main__":
    app.run()
