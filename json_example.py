import json



class DataProcessor():

    def __init__(self, data_source):
        self.data_source = data_source


    def get_data(self):
        return self.data_source()

x = json.loads("""{
  "id": "ID0001",
  "value": "Some value"
}""")

import requests

def from_http():
    response = requests.get("https://raw.githubusercontent.com/majorbriggs/python_training/master/data.json", verify=False)
    return response.json()