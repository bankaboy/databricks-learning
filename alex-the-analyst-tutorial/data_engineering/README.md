Following the [data engineering in databricks](https://www.youtube.com/watch?v=hEv5y_s0L3c) tutorial by alex the analyst

### Lesson 1: Ingesting Data into Databricks
- ELT in Databricks
  - Load the raw data, clean it and prepare it for analytics (Bronze --> Silver -> Gold)
  - Store data in the Delta tables and transform it using SQL, Python or Spark
  - Usually follows ELT: load first , transform inside Databricks

### Lesson 2: Building ETL Pipelines in Databricks
- Bronze: Raw Ingestion
  - raw, unmodified data
  - from all sources
  - landing zone
  - kept as-is forever

- Silver: Cleaned & conformed
  - validated and cleaned
  - deduplicated
  - standardised schema
  - enterprise joins

- Gold: Business Ready
  - aggregated metrics
  - KPIs and dashboards
  - ML Feature store
  - Business logic applied 

### Lesson 3: Job Orchestration:
Can set up pipelines as job or notebooks directly if simpler work. Can set up triggers and schedules and dependencies in a similar fashion to adf.