import requests
import pprint
from data_manager import *
from flight_data import *
from flight_search import *
from notification_manager import *
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()

flight = FlightData()
sheet = flight.get_data()

flight_search = FlightSearch()
notification = NotificationManager()

for place in sheet:

    place["IATA Code"] = flight_search.flight_code(place["City"])
    price = flight_search.flight_checking(place["IATA Code"])
    if float(price) < float(place['Lowest Price']):


        notification.send_sms(
        message=f"Lowest Price alert! Only £{float(price)} to fly from London - LON to {place['City']}-{place['IATA Code']}."
        )

# data_manager.update_sheet_data()
# for row in sheet:
#     print(f"{row['City']}: £{row['Lowest Price']}")
