import os
import httpx
from pprint import pprint as print

class PollinationClient(httpx.Client):
    """
    An HTTP client specific to the Pollination REST API.
    """
    class Endpoints:
        user = '/user'
        accounts = '/accounts'
        accounts_name = accounts + '/{name}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base_url = 'https://api.pollination.cloud'

        self.headers['x-pollination-token'] = os.environ['POLLINATION_API_KEY']

        self.organization = os.environ['POLLINATION_ORG']

    def _org_endpoint(self):
        return (
            self
            .Endpoints
            .accounts_name
            .format_map(dict(name=self.organization))
        )

    def get_organization(self) -> dict:
        res = self.get(self._org_endpoint())

        return res.json()


client = PollinationClient()

org = client.get_organization()

print(org)