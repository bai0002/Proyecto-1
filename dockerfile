# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias necesarias
RUN pip install --no-cache-dir Flask

# Expone el puerto en el que Flask estará escuchando
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]

