Primero instalar Google Cloud CLI (GoogleCloudSDKInstaller)
según el manual https://cloud.google.com/storage/docs/gsutil_install?hl=es-419#windows
Otra guía: https://adamtheautomator.com/gcloud-cli-install/

En el manual, explica que al terminar de instalar, dejar las opciones para iniciar la shell y configurar la instalación. 
El instalador inicia una ventana de la terminal y ejecuta el comando gcloud init. En el nos pedirá seleccionar con qué 
cuenta de google vamos a trabajar y en qué proyecto. Es como autenticarnos.

Adicionalmente, debemos de agregarloal PATH. Run the command .\google-cloud-sdk\install.bat en el mismo cmd que se abrió
anteriormente. 

Guias complementarias completas:
https://adamtheautomator.com/google-cloud-storage-python-client/
https://lynn-kwong.medium.com/how-to-use-gsutil-and-python-to-deal-with-files-in-google-cloud-storage-fc4f430b3b28

----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------

Una vez configurado (si en caso reinicio pc tmb). Cmd: gcloud init
1. Re-initialize this configuration [default] with new settings
2. Picamos que seguimos con el mismo correo
3. Seleccionamos el bucket en el cual trabajamos
4. Do you want to configure a default Compute Region and Zone?: NO
5. Ojo, ya entremos pero aún no tenemos los permisos. Para esto, cmd: gcloud auth application-default login
6. Recién podemos ejecutar python para hacer y deshacer en google cloud storage.
Obs: Este método almacena tus credenciales en un archivo del sistema de archivos. Cualquier usuario con acceso al sistema de 
    archivos puede usar esas credenciales. Cuando ya no necesites estas credenciales, debes revocarlas:
    gcloud auth application-default revoke
Guia: https://cloud.google.com/docs/authentication/provide-credentials-adc?hl=es-419#how-to

----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------

Ahora, desde tu pc podrás enlistar los buckets que tienes en el proyecto. Sin embargo, si quieres enlistar los files dentro
del bucket, crear - eliminar files, etc; primero debes de agregar permisos al correo que usa el environment conectado.
De lo contrario va a aparecer el siguiente error:
403 GET https://storage.googleapis.com/storage/v1/b/bigdata-course/o?projection=noAcl&prefix=landing%2F&prettyPrint=false: 
Victormontesjaramillo2000@gmail.com does not have storage.objects.list access to the Google Cloud Storage bucket. Permission 
'storage.objects.list' denied on resource (or it may not exist).

Para entender más sobre permisos y roles:
GCP has the concept of roles and permissions. A role is something like Storage Admin (roles/storage.admin) and a permission 
is something like storage.buckets.get. Roles are made up of one or more permissions. Permissions are always granted by 
applying a role to a principal (user, service account, or group) -- that is, you cannot assign a permission directly to a 
principal.
The error you're seeing is because the permission storage.buckets.get is missing from the service account -- that is, none 
of the role(s) applied to the service account grant the storage.buckets.get permission. You can list the objects of a bucket 
(storage.objects.list permission) without the ability to list buckets (storage.buckets.get permission).
Therefore you need to assign a role such as roles/storage.admin that has the storage.buckets.get permission. You can also 
create a Custom Role with just that permission if you want to operate with a least-privilege model.

Stackoverflow, sobre el error de Permission 'storage.objects.list' denied:
Go to your bucket's permissions section and open add permissions section for your bucket. For example, insufficient service, 
which gcloud tells you, is;
1234567890-compute@developer.gserviceaccount.com 
Add this service as user then give these roles;
Cloud Storage - Storage Admin
Cloud Storage - Storage Object Admin
Cloud Storage - Storage Object Creator
Then you should have sufficient permissions to make changes on your bucket.

Además:
The following command lists all service accounts associated with a project:
gcloud iam service-accounts list -> Esto te dará el correo developer
Ahora bien, en el error mencionaban el correo personal Victormontesjaramillo2000@gmail.com con el cual inicié sesión
en gcloud.init
AGREGUÉ todos los permisos a ambos, tanto el de inicio de sesión como el correo developer. Los de Cloud Storage y el de 
propietario para no tener inconvenientes.


upload_from_string()
upload_from_file()
upload_from_filename()

https://github.com/googleapis/python-storage/tree/05e07f248fc010d7a1b24109025e9230cb2a7259/samples/snippets

----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------

Curiosidad:
Admisión de comodines para el URI de Cloud Storage
1. Cómo seleccionar todos los archivos en todas las carpetas que comienzan con el prefijo
gs://mybucket/fed-samples/fed-sample*
2. cómo seleccionar solo los archivos con una extensión .csv en la carpeta llamada fed-samples y cualquier subcarpeta de fed-samples
gs://mybucket/fed-samples/*.csv
3. Cómo seleccionar archivos con un patrón de nombres de fed-sample*.csv en la carpeta llamada fed-samples. En este ejemplo, no se 
seleccionan archivos en subcarpetas de fed-samples.
gs://mybucket/fed-samples/fed-sample*.csv