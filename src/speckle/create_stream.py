from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account

# initialise the client
client = SpeckleClient(host="https://speckle.xyz/") # or whatever your host is
# client = SpeckleClient(host="localhost:3000", use_ssl=False) or use local server

# authenticate the client with a token
account = get_default_account()

print(account)
client.authenticate(token=account.token)

# create a new stream. this returns the stream id
new_stream_id = client.stream.create(name="a shiny new stream")

# use that stream id to get the stream from the server
new_stream = client.stream.get(id=new_stream_id)


print(new_stream)