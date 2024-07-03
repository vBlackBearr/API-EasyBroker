from dotenv import load_dotenv, dotenv_values
import json
import http.client

class EasyBrokerAPI:
    def __init__(self):
        load_dotenv()
        self.conn = http.client.HTTPSConnection("api.stagingeb.com")
        self.headers = {
            'X-Authorization': dotenv_values(".env")["API_KEY"],
            'Cookie': 'rp=api.stagingeb.com; source=api.stagingeb.com'
        }

    def get_properties(self):
        self.conn.request("GET", f"/v1/properties", '', self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))

if __name__ == "__main__":
    api = EasyBrokerAPI()
    properties = api.get_properties()
    # print(len(properties.get("content", [])))
    for prop in properties.get("content", []):
        print(prop.get("title", "no title"))
