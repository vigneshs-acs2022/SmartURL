from appwrite.client import Client
from appwrite.services.database import Database
import hashlib
import datetime

client = Client()
client.set_endpoint('https://[APPWRITE-ENDPOINT]') \
      .set_project('[PROJECT-ID]') \
      .set_key('[API-KEY]')

database = Database(client)

def shorten_url(original_url, custom_alias=None, expiration_days=None, user_id=None):
    url_id = custom_alias if custom_alias else hashlib.md5(original_url.encode()).hexdigest()[:6]
    short_url = f"https://short.url/{url_id}"
    
    data = {
        'original_url': original_url,
        'short_url': short_url,
        'custom_alias': custom_alias,
        'created_at': datetime.datetime.now(),
        'expiration_date': (datetime.datetime.now() + datetime.timedelta(days=expiration_days)) if expiration_days else None,
        'user_id': user_id
    }

    result = database.create_document(collection_id='urls', document_id='unique()', data=data)
    return result
