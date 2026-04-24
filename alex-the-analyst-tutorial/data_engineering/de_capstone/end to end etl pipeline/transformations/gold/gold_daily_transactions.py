from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.materialized_view(
    name="gold_daily_transactions",
    comment="Daily transaction aggregates for reporting and analytics",
    cluster_by=["transaction_date"]
)
def gold_daily_transactions():
    """
    Gold layer: Daily transaction metrics.
    Aggregates:
    - Total transactions per day
    - Total revenue per day
    - Average transaction amount
    - Total quantity sold
    - Unique customers per day
    """
    df = spark.read.table("silver_transactions")
    
    return (
        df
        .withColumn("transaction_date", F.to_date("transaction_date"))
        .groupBy("transaction_date")
        .agg(
            F.count("transaction_id").alias("total_transactions"),
            F.sum("total_amount").alias("total_revenue"),
            F.avg("total_amount").alias("avg_transaction_amount"),
            F.sum("quantity").alias("total_quantity_sold"),
            F.countDistinct("customer_id").alias("unique_customers")
        )
        .orderBy("transaction_date")
    )
