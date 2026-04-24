# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


job_to_run_end_to_end_pipeline = Job.from_dict(
    {
        "name": "job to run end to end pipeline",
        "trigger": {
            "pause_status": "UNPAUSED",
            "table_update": {
                "table_names": [
                    "data_engineering.end_to_end.transactions",
                ],
            },
        },
        "tasks": [
            {
                "task_key": "end_to_end_etl_pipeline",
                "pipeline_task": {
                    "pipeline_id": "a87ca4bd-8813-4b62-afcb-9dc1bb76fc35",
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=job_to_run_end_to_end_pipeline, job_id=572154614175181)
# or create a new job using: w.jobs.create(**job_to_run_end_to_end_pipeline.as_shallow_dict())
