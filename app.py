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
    # Verifica se a aplicação está sendo executada no ambiente do GitHub Actions
    import os
    if 'GITHUB_ACTIONS' in os.environ:
        app.run(host='0.0.0.0', port=5000)  # Inicia o servidor Flask em um endereço acessível de qualquer lugar
    else:
        app.run(debug=True)  # Inicia o servidor Flask no modo de depuração se não estiver no ambiente do GitHub Actions
