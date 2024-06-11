from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Página inicial'

@app.route('/api')
def api():
    data = {'message': 'UP'}
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Alterado o host para '0.0.0.0' e adicionado o parâmetro 'port'

