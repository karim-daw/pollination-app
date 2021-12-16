from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account


class Stream:

    def __init__(self, host: str) -> None:
        
        self.host = host
        self.streamId = ""
        self.client = SpeckleClient()
    
    def createStream(self, streamName: str):

        # initialise the client
        client = SpeckleClient(host=self.host) # or whatever your host is
        # client = SpeckleClient(host="localhost:3000", use_ssl=False) or use local server
        self.client = client

        try:
            # authenticate the client with a token
            account = get_default_account()
            client.authenticate(token=account.token)
        except:
            print("Could not find default account...have you installed speckle on your machine?")

        # create a new stream. this returns the stream id
        new_stream_id = client.stream.create(name=streamName)

        # use that stream id to get the stream from the server
        new_stream = client.stream.get(id=new_stream_id)

        print("Created stream with stream id... {}".format(new_stream_id))

        # save stream id to class attribute
        self.streamId = new_stream_id

        return new_stream


