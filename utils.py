import datetime
import requests


class Utils:
    url = "https://data.weather.gov.hk/weatherAPI"

    def connect_api(self):
        headers = {'content-type': 'application/json'}
        params = {'dataType': 'fnd', 'lang': 'en'}
        end_point = "/opendata/weather.php"
        link = (self.url + end_point)
        api_response = requests.get(link, params=params, headers=headers)
        return api_response

    def get_status(self):
        response = self.connect_api()
        return response.status_code

    def get_data(self):
        response = self.connect_api()
        if response.status_code == 200:
            print("\nAPI is connected successfully")
            data = response.json()
            return data
        else:
            print("API is failed")

    @staticmethod
    def get_today():
        current_date = datetime.date.today()
        date_string = current_date.strftime("%Y%m%d")
        return date_string



