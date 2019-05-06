import requests


def add_response(response):
    r = requests.post("https://ttl2019.bowmanjd.com/responses", json=response)
    count = r.json()
    return count


def list_responses():
    r = requests.get("https://ttl2019.bowmanjd.com/responses")
    responses = r.json()
    return responses


add_response(["Something", "Something else", "And something more"])
