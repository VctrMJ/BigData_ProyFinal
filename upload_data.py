from google.cloud import storage

# Create a client object
client = storage.Client()

# Get a reference to the bucket you want to upload to
bucket = client.bucket("bigdata_final1project")

# Create a new blob object
blob = bucket.blob("landing/data.json")

#Upload the file to the bucket
blob.upload_from_filename("./data.json")