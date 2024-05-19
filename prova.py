from pyspark.sql import SparkSession

# Inizializza la sessione Spark
spark = SparkSession.builder \
    .appName("PySpark Test") \
    .getOrCreate()

# Crea un DataFrame di esempio
data = [("John", 25), ("Alice", 30), ("Bob", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Esegui alcune operazioni di base su DataFrame
print("Schema del DataFrame:")
df.printSchema()

print("\nContenuto del DataFrame:")
df.show()

# Calcola la media delle età
avg_age = df.agg({"Age": "avg"}).collect()[0][0]
print("\nMedia delle età:", avg_age)

# Stop della sessione Spark
spark.stop()