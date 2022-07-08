import requests

from configuration import SERVICE_URL

resp = requests.get(SERVICE_URL)

print(resp.json())
