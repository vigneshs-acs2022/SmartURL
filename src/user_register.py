from appwrite.client import Client
from appwrite.services.users import Users

client = Client()
client.set_endpoint('https://[APPWRITE-ENDPOINT]') \
      .set_project('[PROJECT-ID]') \
      .set_key('[API-KEY]')

users = Users(client)

def register_user(email, password, name):
    user = users.create(user_id='unique()', email=email, password=password, name=name)
    return user
