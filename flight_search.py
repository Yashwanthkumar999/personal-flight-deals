import requests

KIWI_API_URL = "https://api.tequila.kiwi.com"
API_KEY = "zw-zdmcmhB8PYbddFuC2JHb_HqHsQjN-"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def flight_code(self, row):
        headers = {"apikey": API_KEY}
        query = {"term": row, "location_types": "city"}
        response3 = requests.get(url=f"{KIWI_API_URL}/locations/query", headers=headers, params=query)
        result1 = response3.json()
        iata = result1["locations"][0]["code"]
        return iata

    def flight_checking(self, city_code):
        import datetime as dt
        tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        next_six_months = (dt.datetime.now() + dt.timedelta(days=30 * 6)).strftime("%d/%m/%Y")
        headers = {"apikey": API_KEY}
        query = {"fly_from": "LON",
                 "fly_to": city_code,
                 "date_from": tomorrow,
                 "date_to": next_six_months,
                 "nights_in_dst_from": 7,
                 "nights_in_dst_to": 28,
                 "one_for_city": 1,
                 "max_stopovers": 0,
                 "curr": "GBP"
                 }
        response = requests.get(url=f"{KIWI_API_URL}/v2/search", headers=headers, params=query)
        result2 = response.json()["data"]
        price = result2[0]["conversion"]["GBP"]
        return price




