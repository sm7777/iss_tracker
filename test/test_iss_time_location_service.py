import unittest
from src.iss_time_location_service import*
from unittest.mock import patch

class IssTimeLocationServiceTests(unittest.TestCase):
    
    def test_get_response_returns_response_from_service_for_astronauts_names(self):
        response = get_response()

        self.assertEqual('success', response['message']) 

    def test_parse_response_returns_timestamp_location_from_given_sample_data(self):
        test_response = {'message': 'success', 'timestamp': 1665302898, 'iss_position': {'longitude': '-153.8883', 'latitude': '-35.9674'}}

        self.assertEqual([1665302898, '-35.9674', '-153.8883'], parse_response(test_response))
    
    def test_parse_response_returns_timestamp_location_from_another_sample_data(self):
        test_response = {'message': 'success', 'timestamp': 1665326285, 'iss_position': {'longitude': '29.7201', 'latitude': '-95.3423'}}

        self.assertEqual([1665326285, '-95.3423', '29.7201'], parse_response(test_response))
    
    @patch("src.iss_time_location_service.get_response")
    def test_get_location_calls_parse_response_and_get_response(self, mock_get_response):
        mock_get_response.return_value = {'message': 'success', 'timestamp': 1665302898, 'iss_position': {'longitude': '-153.8883', 'latitude': '-35.9674'}}
        expected_return = [1665302898, '-35.9674', '-153.8883']

        self.assertEqual(expected_return, parse_response(mock_get_response.return_value))

    @patch("src.iss_time_location_service.get_response")
    def test_get_location_returns_time_in_CT(self, mock_get_response):
        mock_get_response.return_value = {'message': 'success', 'timestamp': 1665342915, 'iss_position': {'longitude': '-95.3423', 'latitude': '29.7205'}}
        expected_time = '02:15PM CT'

        self.assertEqual(expected_time, get_location()[0])

    @patch("src.iss_time_location_service.get_response")
    def test_get_location_returns_place_city_state(self, mock_get_response):
        mock_get_response.return_value = {'message': 'success', 'timestamp': 1665342915, 'iss_position': {'longitude': '-95.3423', 'latitude': '29.7205'}}
        expected_location = 'Houston, United States'

        self.assertEqual(expected_location, get_location()[1])

    @patch("src.iss_time_location_service.get_response")
    def test_get_location_throws_exception_if_service_unreachable(self, mock_get_response_unreachable):
        mock_get_response_unreachable.side_effect = Exception("service is unreachable")

        self.assertRaisesRegex(Exception, 'service is unreachable', get_location)     

    @patch("src.iss_time_location_service.get_response")
    def test_get_location_throws_exception_if_service_returns_access_error(self, mock_get_response_access_error):
        mock_get_response_access_error.side_effect = Exception("access error")

        self.assertRaisesRegex(Exception, 'access error', get_location) 

if __name__ == '__main__':
    unittest.main() 