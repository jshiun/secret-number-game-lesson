from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello():
    return {'message': 'This is a response from the server 😀😃😄😁😆😅😂🤣'}, 200

secret_number = 50
@app.route('/guess/<attempt>', methods=['POST'])
def checkAttempt(attempt):
    print('Attempt:', attempt)
    attempt = int(attempt)
    message = "CORRECT!"
    if attempt < secret_number:
        message = "HIGHER!"
    elif attempt > secret_number:
        message = "LOWER!"
    else:
        message = "CORRECT!"

    return {'message':message}, 201


@app.errorhandler(404)
def not_found(e):
    return {'error': 'Resource {} {} Not Found!'.format(request.method, request.url)}, 404


if __name__ == "__main__":
    app.run(debug=True)
