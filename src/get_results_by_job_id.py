
from pollination_rest_api.pollination import PollinationClient, Payload
from urllib.request import urlretrieve


if __name__ == '__main__':
    client = PollinationClient()

    projectName = 'AnnualDaylight-Shoebox4'
    projectID = '20a54a4a-ec9d-4747-92f1-7bc3049c3b0d'

    res = client.get_runs(projectName,projectID)

    body = res.json()

    for run in body['resources']:
        print(run)
        print("hello")
        run_id = run['id']
        # The selected recipe determines the outputs
        run_output_name = run['status']['outputs'][0]['name']

        # Get a download link for the run output
        res = client.get_run_output(projectName, run_id, run_output_name)
        url = res.json()

        # Save to a local file
        urlretrieve(url, f'{run_id}-{run_output_name}.zip')
