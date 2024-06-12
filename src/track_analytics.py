from appwrite.client import Client
from appwrite.services.database import Database
import datetime

client = Client()
client.set_endpoint('https://[APPWRITE-ENDPOINT]') \
      .set_project('[PROJECT-ID]') \
      .set_key('[API-KEY]')

database = Database(client)

def log_click(short_url, location, device):
    document = database.get_document(collection_id='urls', document_id=short_url)
    if document:
        click_data = {
            'short_url': short_url,
            'timestamp': datetime.datetime.now(),
            'location': location,
            'device': device
        }
        
        analytics_data = {
            'short_url': short_url,
            'click_count': document['click_count'] + 1,
            'click_details': document['click_details'] + [click_data]
        }

        database.update_document(collection_id='analytics', document_id=document['$id'], data=analytics_data)

