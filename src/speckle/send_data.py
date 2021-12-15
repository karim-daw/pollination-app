from specklepy.transports.server import ServerTransport
from specklepy.api import operations

from sample_test_block import Block

# here's the data you want to send
block = Block(length=2, height=4)

# next create a server transport - this is the vehicle through which you will send and receive
transport = ServerTransport(client=client, stream_id=new_stream_id)

# this serialises the block and sends it to the transport
hash = operations.send(base=block, transports=[transport])

# you can now create a commit on your stream with this object
commid_id = client.commit.create(
    stream_id=new_stream_id, 
    obj_id=hash, 
    message="this is a block I made in speckle-py",
    )