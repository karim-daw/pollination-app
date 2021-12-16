from specklepy.api.credentials import StreamWrapper
from specklepy.api import operations
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account, get_local_accounts
import json

all_accounts = get_local_accounts() # get back a list
account = get_default_account()

# provide any stream, branch, commit, object, or globals url
wrapper = StreamWrapper("https://speckle.xyz/streams/f1096e83ac/commits/74e202d52c")

# get an authenticated SpeckleClient if you have a local account for the server
client = wrapper.get_client()
client.authenticate(token=account.token)

# get the specified commit data
commit = client.commit.get(wrapper.stream_id, wrapper.commit_id)

# get an authenticated ServerTransport if you have a local account for the server
transport = wrapper.get_transport()

res = operations.receive(commit.referencedObject, transport)

# tests
print(res.get_dynamic_member_names())

topFloorSurface = []
for floor in res['@Floor']:
    for vert in floor.Vertices:
        print(vert.z)
