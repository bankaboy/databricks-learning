from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(
    name="bronze_transactions",
    comment="Raw transaction data ingested from source table"
)
def bronze_transactions():
    """
    Bronze layer: Ingest raw transaction data from source table.
    This is a streaming table for incremental processing.
    """
    return spark.readStream.table("transactions")
