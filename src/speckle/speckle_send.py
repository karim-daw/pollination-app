from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account

# initialise the client
client = SpeckleClient(host="https://speckle.xyz/") # or whatever your host is
# client = SpeckleClient(host="localhost:3000", use_ssl=False) or use local server

# authenticate the client with a token
account = get_default_account()

print(account)
client.authenticate(token=account.token)
