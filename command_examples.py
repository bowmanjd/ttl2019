import json
from subprocess import check_output

# https://docs.python.org/3/library/subprocess.html#subprocess.check_output

# I like to pass in the command as a list of arguments,
# which makes for easy programmatic appending or
# slicing of args
def show_kernel_info():
    cmd = ["uname", "-a"]
    output = check_output(cmd)
    return output


def show_ip_info():
    cmd = ["ip", "addr"]
    output = check_output(cmd)
    return output


def list_responses():
    cmd = ["curl", "https://ttl2019.bowmanjd.com/responses"]
    output = check_output(cmd)
    responses = json.loads(output)
    return responses
