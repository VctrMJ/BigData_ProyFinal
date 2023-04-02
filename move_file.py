from google.cloud import storage

def move_files(folder_ini,folder_fin):

    storage_client = storage.Client()

    bucket = storage_client.bucket('bigdata_final1project')
    blobs = bucket.list_blobs(prefix=folder_ini,)

    for blob in blobs:
        indicador=str(blob.name).split('/')[1]
        if indicador=='':
            pass
        else:
            bucket.rename_blob(blob, new_name=blob.name.replace(folder_ini, folder_fin))
            print('El archivo',indicador,'se movió del folder',folder_ini,'al folder',folder_fin,'\n')
move_files('landing/','bronze/')
move_files('bronze/','silver/')
#CREATE A BUCKET
# # Imports the 'storage' module from the google.cloud package
# # to allow interactions with the Google Cloud Storage.
# from google.cloud import storage
# # Creates a Client object that allows the script to communicate
# # with Google Cloud Storage and perform operations on it (like creating a bucket).
# client = storage.Client()
# # Creates a new bucket with a specified name
# bucket = client.create_bucket("my-first-3333333")
# # Prints a message indicating the bucket was successfully created.
# print("Bucket {} created.".format(bucket.name))
