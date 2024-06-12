from datetime import datetime
from appwrite.services.databases import Databases
from appwrite_client import get_client

def handler(req, res):
    client = get_client()
    database = Databases(client)
    
    urls = database.list_documents('databaseId', 'URLs')
    now = datetime.utcnow()
    
    for url in urls['documents']:
        expiration_date = url.get('expirationDate')
        if expiration_date and datetime.strptime(expiration_date, '%Y-%m-%dT%H:%M:%S.%fZ') < now:
            database.update_document('databaseId', 'URLs', url['$id'], {'isActive': False})
    
    res.json({'success': True})
