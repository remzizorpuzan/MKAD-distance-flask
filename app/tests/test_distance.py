from routes.distance import API_KEY
import unittest
import requests


class TestAPI(unittest.TestCase):

    BASE_URL = 'https://geocode-maps.yandex.ru/1.x/?apikey=' + \
        API_KEY+'&format=json&geocode='
    response = requests.get(BASE_URL)

    def test_input(self):
        # Test for status 200
        resp = requests.get(self.BASE_URL+"Istanbul")
        self.assertEqual(resp.status_code, 200)

    def test_empty(self):
        # Test for empty input
        resp = requests.get(self.BASE_URL+"")
        self.assertEqual(resp.status_code, 400)

    def test_invalid_input_symbol(self):
        # Test for invalid symbol inputs
        test_response_symbol = requests.get(self.BASE_URL+"-")
        test_json_symbol = test_response_symbol.json()
        test_object_symbol = test_json_symbol["response"]["GeoObjectCollection"][
            "metaDataProperty"]["GeocoderResponseMetaData"]["found"]
        self.assertEqual(test_object_symbol, "0")

    def test_invalid_input_int(self):
        # Test for invalid integer inputs
        test_response_int = requests.get(self.BASE_URL+"9")
        test_json_int = test_response_int.json()
        test_object_int = test_json_int["response"]["GeoObjectCollection"][
            "metaDataProperty"]["GeocoderResponseMetaData"]["found"]
        self.assertEqual(test_object_int, "0")
