# Use uma imagem base do Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o container
COPY ./requirements.txt /app/requirements.txt
COPY ./src /app/src
COPY ./main.py /app/main.py

# Instala as dependências
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Expõe a porta usada pela FastAPI
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
