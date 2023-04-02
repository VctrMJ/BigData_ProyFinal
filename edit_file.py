from google.cloud import storage

def write_read(bucket_name, blob_name):
    """Write and read a blob from GCS using file-like IO"""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your new GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Mode can be specified as wb/rb for bytes mode.
    # See: https://docs.python.org/3/library/io.html
    

    # with blob.open("w") as f:
    #     f.write("Hello world")
    bucket.rename_blob(blob, new_name=blob.name.replace('json', 'csv'))
    # with blob.open("r") as f:
    #     print(f.read())
    
write_read('bigdata_final1project','probooo.json')