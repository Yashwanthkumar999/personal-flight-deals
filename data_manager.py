import requests
from pprint import pprint

SHHET_URL = "https://api.sheety.co/0a12e291e32eae5d60922513c366c4cb/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.documents_data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHHET_URL)
        final_sheet = response.json()
        self.documents_data = final_sheet['prices']
        return self.documents_data

    # def update_sheet_data(self):
    #     for place in self.documents_data:
    #         new_data = {
    #             "price": {
    #                 "iataCode": place["iataCode"]
    #             },
    #         }
    #
    #         requests.put(url=f"{SHHET_URL}/{place['id']}", json=new_data)









