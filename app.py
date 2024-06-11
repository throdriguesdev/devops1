from flask import Flask, jsonify

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return 'test'

# Rota para uma página de saudação com JSON
@app.route('/api')
def api():
    data = {'message': 'UP'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
