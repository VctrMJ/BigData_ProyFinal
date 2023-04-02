#pip install google-api-python-client
#Google console -> nuevo proyecto -> habilitar YouTube Data API v3 -> generar credencial
#LISTO!
import googleapiclient.discovery
import pprint as pprint
import json

#API information
api_service_name="youtube"
api_version="v3"
DEVELOPER_KEY="...."

#API cliente
youtube = googleapiclient.discovery.build(api_service_name,api_version,developerKey=DEVELOPER_KEY)

#Request body
#URL of Video: https://www.youtube.com/watch?v=0sad55as6
#Video de El Chombo
request = youtube.videos().list(
    part='statistics',
    id='md4sROsF0yg'
)

#Request execution
response = request.execute()
dicc_info=response['items'][0]['statistics']
jsonString=json.dumps(dicc_info)
with open ('data.json','w') as f:
    json.dump(jsonString,f)
