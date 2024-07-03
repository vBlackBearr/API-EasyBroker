from dotenv import load_dotenv, dotenv_values
import json
import http.client

load_dotenv()

conn = http.client.HTTPSConnection("api.stagingeb.com")
payload = ''
headers = {
  'X-Authorization': dotenv_values(".env")["API_KEY"],
  'Cookie': 'rp=api.stagingeb.com; source=api.stagingeb.com'
}
conn.request("GET", "/v1/properties?page=1&limit=20", payload, headers)
res = conn.getresponse()
data = res.read()

data_json = json.loads(data.decode("utf-8"))

print("\n-- Printing the keys of the JSON object:\n--")
print(list(data_json.keys()))

print("\n-- Printing keys of the first object in the content array:\n--")
print(list(data_json["content"][0].keys()))