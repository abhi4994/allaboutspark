1- Install docker desktop from the link below , install and open the application:
https://www.docker.com/products/docker-desktop/

2- Create following files and folders structure inside spark-bootcamp folder in your computer at any path.

### ├── docker-compose.yml

### ├── jupyter/

           └── Dockerfile

### ├── notebooks/

### ├── data/

           └── orders.csv

### ├──event-logs/

### ├──spark-conf/

           └── spark-defaults.conf

3- Now open windows power shell/ Mac terminal change directory to spark-bootcamp
Run following commands:  
# Build containers (first time only)
docker compose build

# Start Spark Master, Workers, Jupyter
docker compose up -d


4- Now you should be able to access services on below ports :

Jupyter Lab → http://localhost:8888/

Driver UI → http://localhost:4040

Spark Master UI → http://localhost:8080

Worker 1 UI → http://localhost:8081

Worker 2 UI → http://localhost:8082

# Stop the cluster when done:
docker compose down

# start again when needed 
docker compose up -d

5- On Jupyter lab rub following code to verify:

from pyspark.sql import SparkSession
spark = (
SparkSession.builder.master("spark://spark-master:7077").appName("spark-session-mac").getOrCreate()
)

spark

It should display spark version. 

