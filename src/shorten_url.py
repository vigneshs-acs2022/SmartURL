from appwrite.client import Client
from appwrite.services.databases import Databases
import hashlib
import datetime
import json
import asyncio

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1') \
      .set_project('666927680026e4e78388') \
      .set_key('f00160675e58ed23e0332fecf4a1ff21b84e73fb959c92cd155b2d1607c3333420cc3f742e73732448fa97ff78322b254bd880a8e667293f6ae0bd408fca1d0a91584b065e59b80bedf6daa5ffe5d410378433f7c46b4cffb90cda8a95b0b75f1018eb72f83cf7f8b6d6fbc573c3681e3672c4da76c8c5ca6ac8dd4f8291be5a')


database = Databases(client)

def shorten_url(original_url, custom_alias=None, expiration_time=None, user_id=None):
    url_id = custom_alias if custom_alias else hashlib.md5(original_url.encode()).hexdigest()[:6]
    short_url = f"https://short.url/{url_id}"
    
    data = {
        'original_url': original_url,
        'short_url': short_url,
        'custom_alias': custom_alias,
        'created_at': datetime.datetime.now(),
        'expiration_date': expiration_time,
        'user_id': user_id
    }

    result = database.create_document(collection_id='urls', document_id='unique()', data=data)
    return result


async def main(context=None):
    data={
    "originalURL": "https://example.com",
    "user_id": 1,
    "custom_alias": "exampleAlias",
    "expiration_time":"2024-06-12 01:01:10"
}

    payload = data
    originalURL = payload.get('originalURL')
    user_id = payload.get('user_id')
    custom_alias = payload.get('custom_alias')
    expiration_time = payload.get('expiration_time')

    shorten_url(originalURL,custom_alias,expiration_time,user_id)
