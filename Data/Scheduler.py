from dagster import job, op, repository, ScheduleDefinition
import PredData

@op
def my_op():
    PredData.DataPipeline()

@job
def Stock_Data_job():
    my_op()

# Step 4: Define the schedule for the job
my_schedule = ScheduleDefinition(
    job=Stock_Data_job,
    cron_schedule="0 23 * * *",  # At 23:00 (11 PM) every day
    execution_timezone="UTC"  # Specify the timezone, adjust as needed
)

# Step 5: Define the repository
@repository
def my_repository():
    return [Stock_Data_job, my_schedule]
