import random
import string
from appwrite.services.databases import Databases
from appwrite_client import get_client

def handler(req, res):
    client = get_client()
    database = Databases(client)
    
    data = req.json
    original_url = data.get('originalURL')
    custom_alias = data.get('alias')
    user_id = data.get('userID')
    
    shortened_url = custom_alias or generate_short_url()
    
    result = database.create_document(
        'databaseId',
        'URLs',
        'unique()',
        {
            'originalURL': original_url,
            'shortenedURL': shortened_url,
            'alias': custom_alias,
            'expirationDate': None,
            'userID': user_id
        }
    )
    
    res.json({'shortenedURL': shortened_url})

def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
