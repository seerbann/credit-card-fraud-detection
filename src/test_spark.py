from pyspark.sql import SparkSession

def main():
    print("Initializing Spark Session...")
    # 1. Start a Spark Session
    spark = SparkSession.builder \
        .appName("AnomalyDetectionSetup") \
        .getOrCreate()

    # 2. Define the path to your dataset
    # Make sure creditcard.csv is placed exactly in this folder!
    file_path = "../data/creditcard.csv"

    try:
        print("Loading dataset...")
        # 3. Read the CSV file
        # inferSchema=True automatically detects if a column is a string, integer, or float
        df = spark.read.csv(file_path, header=True, inferSchema=True)

        # 4. Print the schema (column names and data types)
        print("\n--- DATA SCHEMA ---")
        df.printSchema()

        # 5. Show the first 5 rows
        print("\n--- FIRST 5 ROWS ---")
        df.show(5)

        # 6. Quick Anomaly Check
        # The 'Class' column contains 0 for normal and 1 for fraud.
        print("\n--- CLASS DISTRIBUTION (Normal vs Fraud) ---")
        df.groupBy("Class").count().show()

    except Exception as e:
        print(f"\nError loading the data: {e}")
        print("Did you remember to download the Kaggle dataset and put it in data/raw/creditcard.csv?")

    finally:
        # 7. Stop Spark
        spark.stop()

if __name__ == "__main__":
    main()