import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req.status_code)

if post_codes_req.status_code == 200:
    print("Success")
elif post_codes_req.status_code == 404:
    print("Sorry page not available!")