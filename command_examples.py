import json
from subprocess import check_output


def list_responses():
    output = check_output(["curl", "https://ttl2019.bowmanjd.com/responses"])
    responses = json.loads(output)
    return responses
