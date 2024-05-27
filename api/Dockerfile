# Utiliza la imagen base de CUDA
FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

# Actualiza el repositorio de apt e instala dependencias necesarias
RUN apt-get -qq update && \
    apt-get -qq install -y --no-install-recommends \
    build-essential \
    python3-pip \
    python3-venv \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Crear y activar un entorno virtual
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instala los paquetes Python necesarios
RUN pip install --upgrade pip && \
    pip install pycuda flask numpy

# Copiar el código de la aplicación al contenedor
COPY . /app
WORKDIR /app

# Expone el puerto en el que corre la aplicación Flask (opcional)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
