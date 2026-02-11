Weekly learning sessions to learn the capabilities of databricks and to keep notes
Session: 30 Jan 2026

* Delta lakes give follow the ACID properties - atomic, consistent, isolated, durable.
* Best practice of naming notebook: &lt;env&gt;\_&lt;layer&gt;\_&lt;about&gt;_&lt;the work done&gt;.
* Whatever you create will directly be covered by unity catalogue and stored as delta tables (allows acid transactions and time travel).
* Delta tables store the information as parquet but have additional information about changes done in JSON.
* Different types of cluster options - Serverless, SQL Warehouse, All Purpose (for interacting with notebooks, not advisable for test/prod), Job Compute (cluster is auto closed one job is finished).
* Change data feed, capture the changes that occur in the table between different versions. update_preimage and update_postimage provide the status of the table/row before and after the update.