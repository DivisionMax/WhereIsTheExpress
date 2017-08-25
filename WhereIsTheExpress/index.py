from flask import Flask, render_template
import yaml
from pprint import pprint
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


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
