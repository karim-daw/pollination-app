from specklepy.transports.server import ServerTransport
from specklepy.api import operations

from sample_test_block import Block
from create_stream import Stream

# init stream with host server
myStream = Stream("https://speckle.xyz/")

# create stream
myStream.createStream("Karim's Brand new stream")

# get speckle client from stream
myClient = myStream.client

# get stream Id
myStreamId = myStream.streamId

# here's the data you want to send
block = Block(length=2, height=4)

# next create a server transport - this is the vehicle through which you will send and receive
transport = ServerTransport(client=myClient, stream_id=myStreamId)

# this serialises the block and sends it to the transport
hash = operations.send(base=block, transports=[transport])

# you can now create a commit on your stream with this object
commid_id = myClient.commit.create(
    stream_id=myStreamId, 
    object_id=hash, 
    message="this is a block I made in speckle-py",
    )