import json

from task import Task
from dateutils import get_current_timestamp, to_unix_timestamp

def handler(event, context):
    task = (
        Task()
            .label("Do the homework")
            .created_at(to_unix_timestamp(get_current_timestamp()))
            .to_json_format()
    ),

    return {
        "statusCode": 200,
        "body": json.dumps({
            "task": task
        })
    }
