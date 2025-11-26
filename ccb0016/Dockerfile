FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /ccb0016

# Copiamos requirements e instalamos dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# Exponemos el puerto 3000 (como indica docker-compose)
EXPOSE 8081

# Comando para ejecutar la app
CMD ["python", "app.py"]
