from data_manager import *
import os
import pandas
import csv


SHHET_URL = "https://api.sheety.co/27466de634e89a5ad5d83cda48cdd619/flightDeals/prices"


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):

        self.flight_data = {}

    def get_data(self):
        with open("Flight Deals - prices.csv", newline='') as data_file:
            reader = csv.DictReader(data_file)
            data = [row for row in reader]
            self.flight_data = data
            return self.flight_data

    # def update_data(self):
    #      for place in self.flight_data:
    #          place["Lowest Price"] = ""
    #          place["IATA Code"] = self.flight_data(place["City"])
    #          place["Lowest Price"] = flight_search.flight_checking(place["IATA Code"])

















