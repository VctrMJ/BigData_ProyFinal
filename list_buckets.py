from google.cloud import storage

# Create a client object
client = storage.Client()

# List all the buckets in your project
buckets = list(client.list_buckets())

# Print name of buckets
for bucket in buckets:
    print(bucket.name)