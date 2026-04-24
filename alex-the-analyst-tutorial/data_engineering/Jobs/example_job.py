# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


Silver_to_Gold_Job = Job.from_dict(
    {
        "name": "Silver to Gold Job",
        "schedule": {
            "quartz_cron_expression": "57 45 7 ? * Wed",
            "timezone_id": "Europe/London",
            "pause_status": "UNPAUSED",
        },
        "tasks": [
            {
                "task_key": "Bronze_to_silver",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/piku21081999@outlook.com/databricks-learning/alex-the-analyst-tutorial/data_engineering/(Org) Bronze to Silver Transformation",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Bronze_to_silver_to_gold",
                "pipeline_task": {
                    "pipeline_id": "4d8ae269-4b0e-403d-a943-d3560687ac6b",
                    "full_refresh": False,
                },
            },
            {
                "task_key": "Silver_to_gold",
                "depends_on": [
                    {
                        "task_key": "Bronze_to_silver",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/piku21081999@outlook.com/databricks-learning/alex-the-analyst-tutorial/data_engineering/(Org) Silver to Gold Transformation",
                    "source": "WORKSPACE",
                },
            },
        ],
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=Silver_to_Gold_Job, job_id=1073157130496670)
# or create a new job using: w.jobs.create(**Silver_to_Gold_Job.as_shallow_dict())
