# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
# 1. Import required Spark SQL functions
from pyspark.sql.functions import col, current_date

# 2. Create a simple sample dataset (Sales Data)
data = [
    (1, "Electronics", 750.00, "Mumbai"),
    (2, "Apparel", 120.50, "Delhi"),
    (3, "Electronics", 1200.00, "Bangalore"),
    (4, "Home Decor", 340.25, "Chennai"),
    (5, "Apparel", 89.90, "Hyderabad")
]

# 3. Define schema column names
columns = ["TransactionID", "Category", "Amount", "City"]

# 4. Create the Spark DataFrame
df = spark.createDataFrame(data, schema=columns)

# 5. Add a calculated column for tracking the run date
final_df = df.withColumn("ProcessedDate", current_date())

# 6. Display the results in the notebook output window
print("--- Sample Data Generated Successfully ---")
display(final_df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
