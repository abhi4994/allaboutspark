⭐  spark-local-setup  ⭐

# 🚀 Spark Local Setup using Docker & Jupyter

This guide helps you set up **Apache Spark** locally using **Docker Compose** and access it via **JupyterLab** for development and testing.

---

## 📌 Prerequisites

- **Docker Desktop** installed and running
  👉 Download from: https://www.docker.com/products/docker-desktop/

- Windows (PowerShell) or macOS/Linux (Terminal)

---

## 📂 Project Structure

Create a folder named **`spark-setup`** at any location on your system and set up the following directory structure:

├── docker-compose.yml

├── jupyter/
       
       └── Dockerfile
       
├── notebooks/
       
├──event-logs/

├──spark-conf/
       
       └── spark-defaults.conf


## ▶️ Starting the Spark Cluster

1. Open **Windows PowerShell** or **Mac/Linux Terminal**
2. Navigate to the `spark-setup` directory:

cd path/to/spark-setup


## ▶️ Build containers (One time only)

    command: docker compose build

## ▶️ Start the Spark cluster in detached mode:

    command: docker compose up -d

🌐 Spark Web UI : Once the cluster is up, you can access the Spark UIs in your browser:

    Jupyter Lab → http://localhost:8888/

    Driver UI → http://localhost:4040

    Spark Master UI → http://localhost:8080

    Worker 1 UI → http://localhost:8081

    Worker 2 UI → http://localhost:8082

⏹️ Stopping the Cluster

    command: docker compose down

## ▶️ start again when needed

    command: docker compose up -d

📓 Verifying Spark in JupyterLab

Open JupyterLab from your browser (as configured in Docker).
Create or open a notebook.
Run the following PySpark code:

"""
    
    from pyspark.sql import SparkSession
    spark = (
        SparkSession.builder
        .master("spark://spark-master:7077")
        .appName("spark-app")
        .getOrCreate()
    )

    spark

"""

✅ If successful, the output will display the Spark version and session details, confirming that Spark is running correctly.
🎯 You're All Set!

You now have a fully functional local Spark environment with Docker and JupyterLab.
Happy Spark-ing! 🔥


