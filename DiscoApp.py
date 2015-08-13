from flask import Flask
#from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(debug=True)
