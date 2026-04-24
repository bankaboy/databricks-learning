from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(
    name="silver_transactions",
    comment="Cleaned and standardized transaction data"
)
@dp.expect("valid_transaction_id", "transaction_id IS NOT NULL")
@dp.expect("valid_amount", "total_amount > 0")
@dp.expect("valid_quantity", "quantity > 0")
def silver_transactions():
    """
    Silver layer: Clean and standardize the bronze transaction data.
    - Trim whitespace from string fields
    - Standardize casing (proper case for product names, title case for categories)
    - Filter out invalid records
    """
    df = spark.readStream.table("bronze_transactions")
    
    return (
        df
        .withColumn("transaction_date", F.col("transaction_date").cast("timestamp"))
        .withColumn("product_name", F.initcap(F.trim(F.regexp_replace("product_name", "\\s+", " "))))
        .withColumn("category", F.initcap(F.trim(F.col("category"))))
        .withColumn("store_location", F.initcap(F.trim(F.col("store_location"))))
        .withColumn("payment_method", F.initcap(F.trim(F.col("payment_method"))))
        .filter("transaction_id IS NOT NULL")
    )
