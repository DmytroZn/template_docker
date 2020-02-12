# from flask import Flask, escape, request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    print('hu')
    return 'Hello everyone'



if __name__ == '__main__':
    app.run(port=5000, debug=True)