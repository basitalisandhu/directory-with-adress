import unittest
import requests
from unittest.mock import patch, Mock
from app.api import get_place_id, get_place_phone_number
from json import loads


class ApiTest(unittest.TestCase):
    API_URL = 'http://localhost:5000/getphonenumber?address='
    addresses = []


    def test_get_place_id(self):
        mock_get_patcher = patch('app.api.requests.get')
        place_details = '{\n   "candidates" : [\n      {\n         "formatted_address" : "6101 W Century Blvd, Los Angeles, CA 90045, United States",\n         "name" : "Sheraton Gateway Los Angeles Hotel",\n         "place_id" : "ChIJWQrR4tS2woARHV9LcAjcw48"\n      }\n   ],\n   "status" : "OK"\n}\n'
        mock_get = mock_get_patcher.start()
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = place_details
        place = "Sheraton Gateway Los Angeles Hotel"
        response = get_place_id(place)
        mock_get_patcher.stop()
        try:
            self.assertEqual(response,'ChIJWQrR4tS2woARHV9LcAjcw48', "Failed! Respose does not match the actual outcome.")
        except AssertionError as error:
            print(error)


    def test_get_place_phone_number(self):
        mock_get_patcher = patch('app.api.requests.get')
        place_details = '{\n   "html_attributions" : [],\n   "result" : {\n      "formatted_phone_number" : "(310) 642-1111",\n      "name" : "Sheraton Gateway Los Angeles Hotel"\n   },\n   "status" : "OK"\n}\n'
        mock_get = mock_get_patcher.start()
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = place_details
        place_id = 'ChIJWQrR4tS2woARHV9LcAjcw48'
        response = get_place_phone_number(place_id)
        mock_get_patcher.stop()
        try:
            self.assertEqual(response,'(310) 642-1111', "Failed! Respose does not match the actual outcome.")
        except AssertionError as error:
            print(error)


if __name__ == "__main__":
    unittest.main()