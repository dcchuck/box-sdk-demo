"""
"""
from dotenv import load_dotenv
from boxsdk import OAuth2, Client
from os import environ

load_dotenv()

# The OAuth takes an access token but the UI calls it a developer token
auth = OAuth2(
    client_id=environ.get('CLIENT_ID'),
    client_secret=environ.get('CLIENT_SECRET'),
    access_token=environ.get('DEVELOPER_TOKEN'),
)
client = Client(auth)

user = client.user().get()
print(f'The current user ID is {user.id}')