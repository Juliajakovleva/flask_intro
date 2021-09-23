from flask import Flask, app

app = Flask(__name__)

@app.route('/')
def home():
    return "Sveika, svetdiena!"

@app.route('/kontakti')
def kontakti():
    return "<html><h1>Kontakti</h1><p>Yulia Yakovleva</p></html>"

if __name__ == '__main__':
    app.run(port=80, debug=True)