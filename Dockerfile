# Use a imagem base do Python 3.9
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . /app

# Atualiza o pip
RUN pip install --upgrade pip

# Instala as dependências listadas no requirements.txt
RUN pip install -r requirements.txt

# Comando padrão para executar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
