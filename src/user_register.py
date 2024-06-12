from appwrite.client import Client
from appwrite.services.users import Users
import asyncio

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1') \
      .set_project('666927680026e4e78388') \
      .set_key('f00160675e58ed23e0332fecf4a1ff21b84e73fb959c92cd155b2d1607c3333420cc3f742e73732448fa97ff78322b254bd880a8e667293f6ae0bd408fca1d0a91584b065e59b80bedf6daa5ffe5d410378433f7c46b4cffb90cda8a95b0b75f1018eb72f83cf7f8b6d6fbc573c3681e3672c4da76c8c5ca6ac8dd4f8291be5a')

users = Users(client)

async def user_register():
    name = "vignesh"
    email = "vigneshsankar+12@agilecybersolutions.com"
    password = "12345"
    user = await users.create(user_id='unique()', email=email, password=password, name=name)
    print("User registered successfully")
    return user

async def main(context=None):
    await user_register()

if __name__ == "__main__":
    asyncio.run(main())
