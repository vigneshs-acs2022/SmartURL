from appwrite.client import Client

def get_client():
    client = Client()
    client.set_endpoint('http://localhost/v1')  # Your API Endpoint
    client.set_project('projectId')  # Your project ID
    client.set_key('apiKey')  # Your secret API key
    return client
