FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.8, pip, Java 17
RUN apt-get update && \
    apt-get install -y python3.8 python3.8-distutils python3-pip openjdk-17-jdk wget curl && \
    apt-get clean

# Tell PySpark to use Python 3.8
ENV PYSPARK_PYTHON=python3.8
ENV PYSPARK_DRIVER_PYTHON=python3.8


# Install Jupyter + PySpark (match Spark 3.5.1)
RUN pip3 install --no-cache-dir notebook jupyterlab pyspark==3.5.1


# Working directory
WORKDIR /workspace

EXPOSE 8888 4040

# Disable token and password
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=", "--NotebookApp.password="]
