from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/hello')
def hello():
    return {
        'hello':'hello linh'
    }

if __name__ == "__main__":
    app.run(debug=True)