from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account


class Stream:

    def __init__(self, host: str) -> None:
        
        self.host = host
        self.streamId = ""

        # initialise the client
        self.client = SpeckleClient(host=self.host)
    
    def createStream(self, streamName: str):
        """ creates a speckle by given stream name and returns stream """

        try:
            # authenticate the client with a token
            account = get_default_account()
            self.client.authenticate(token=account.token)
        except:
            print("Could not find default account...have you installed speckle on your machine?")

        # create a new stream. this returns the stream id
        new_stream_id = self.client.stream.create(name=streamName)

        # use that stream id to get the stream from the server
        new_stream = self.client.stream.get(id=new_stream_id)

        print("Created stream with stream id... {}".format(new_stream_id))

        # save stream id to class attribute
        self.streamId = new_stream_id

        return new_stream


