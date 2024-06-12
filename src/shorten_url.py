from appwrite.client import Client
from appwrite.services.databases import Databases
import hashlib
import datetime
import json
import asyncio
import pyshorteners

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1') \
      .set_project('666927680026e4e78388') \
      .set_key('f00160675e58ed23e0332fecf4a1ff21b84e73fb959c92cd155b2d1607c3333420cc3f742e73732448fa97ff78322b254bd880a8e667293f6ae0bd408fca1d0a91584b065e59b80bedf6daa5ffe5d410378433f7c46b4cffb90cda8a95b0b75f1018eb72f83cf7f8b6d6fbc573c3681e3672c4da76c8c5ca6ac8dd4f8291be5a')

database_id = "6669283a00091f8628fa"
collection_id = "666928b50030f4d1282d"
database = Databases(client)

def shorten_url(context,original_url, custom_alias=None, expiration_time=None, user_id=None):
    short_url = pyshorteners.Shortener().tinyurl.short(original_url)
    
    data = {
        'originalURL': original_url,
        'shortenedURL': short_url,
        'alias': custom_alias,
        # 'expiration_date': expiration_time.isoformat() if isinstance(expiration_time, datetime) else expiration_time,
        'users': [user_id]
    }

    result = database.create_document( database_id=database_id,collection_id=collection_id, document_id='unique()', data=data)
    return result


async def main(context=None):
    payload = context.req

    originalURL = payload.get('originalURL')
    user_id = payload.get('user_id')
    custom_alias = payload.get('custom_alias')
    expiration_time = payload.get('expiration_time')

    response = shorten_url(context,originalURL,custom_alias,expiration_time,user_id)

    return context.res.json(response)