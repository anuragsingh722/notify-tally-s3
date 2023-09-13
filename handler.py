import json

from motoezzy import Motoezzy


def notify_file_push(event, context):
    record = event.get("Records")[0]
    bucket_name = record.get("s3").get("bucket").get("name")
    object_key = record.get("s3").get("object").get("key")

    body = {
        "bucket": bucket_name, "key": object_key
    }

    motoezzy = Motoezzy()
    motoezzy.invoice_upload_notification(bucket=bucket_name, file_path=object_key)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
