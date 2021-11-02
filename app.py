from flask import Flask 
app = Flask(__name__)


@app.route("/")
def home():
    return 'Hi World'

@app.route("/page")
def page():
    return 'This is my page'

if __name__=="__main__":
    app.run()