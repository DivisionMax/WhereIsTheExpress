from flask import Flask, render_template
import yaml
app = Flask(__name__)

secret = None
clint_id = None
with open("config.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
        secret = config['auth']['secret']
        client_id = config['auth']['client-id']
    except yaml.YAMLError as exc:
        print(exc)


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
