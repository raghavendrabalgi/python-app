import requests 
import urllib3 
from certifi import where

def get_external_ip():
    response = requests.get("https://api.ipify.org?format=json")
    ip = response.json()["ip"]
    return ip

def main():
    print(f"My external IP is: {get_external_ip()}")
    print(getList("https://google.com"))

def getList(listUrl):
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',  # Force certificate check.
        ca_certs=where(),  # Path to the Certifi bundle.
    )

    data = http.request('GET', listUrl, timeout=10).data
    return data

if __name__ == "__main__":
    main()

