import json
import uuid
import random
from datetime import datetime, timedelta
import boto3

MINIO_ENDPOINT = "http://localhost:9000"
ACCESS_KEY = "minioadmin"
SECRET_KEY = "minioadmin123"
BUCKET_NAME = "bronze"

NUM_RECORDS = 1000000

s3 = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

filename = "raw_events.jsonl"

event_types = [
    "view_item",
    "add_to_cart",
    "checkout",
    "purchase"
]

start_date = datetime.now()

with open(filename, "w") as f:
    for _ in range(NUM_RECORDS):
        record = {
            "event_id": str(uuid.uuid4()),
            "timestamp": (
                start_date
                - timedelta(seconds=random.randint(0, 86400))
            ).isoformat(),
            "user_id": random.randint(1, 100000),
            "event_type": random.choice(event_types),
            "product_id": random.randint(1, 5000),
            "price": round(random.uniform(10, 1000), 2)
        }

        f.write(json.dumps(record) + "\n")

print("Generated 1,000,000 records")

s3.upload_file(
    filename,
    BUCKET_NAME,
    filename
)

print("Uploaded to MinIO Bronze bucket")