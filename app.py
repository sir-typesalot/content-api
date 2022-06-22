from flask import Flask
from endpoints.routes import app

if __name__ == '__main__':
    # Multi threading option enabled
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)