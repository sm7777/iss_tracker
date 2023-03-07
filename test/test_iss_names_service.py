import unittest
from unittest.mock import patch
from src.iss_names_service import*

class IssNamesServiceTests(unittest.TestCase):

    def test_get_response_returns_response_from_service_for_astronauts_names(self):
        response = get_response()

        self.assertEqual('success', response['message']) 

    def test_parse_response_returns_astronauts_names_from_the_given_sample_data(self):
        test_response = {'number': 14, 'message': 'success', 'people': [{'craft': 'ISS', 'name': 'Mark Watney'}, {'craft': 'Millenium Falcon', 'name': 'Han Solo'}, {'craft': 'ISS', 'name': 'Paul Atreides'}]}

        self.assertEqual([('Mark', 'Watney'), ('Paul', 'Atreides')], parse_response(test_response))

    def test_parse_response_returns_astronauts_names_from_another_given_sample_data(self):
        test_response = {'number': 26, 'message': 'success', 'people': [{'craft': 'Enterprise', 'name': 'Jean-Luc Picard'}, {'craft': 'ISS', 'name': 'Mike Massimino'}, {'craft': 'Death Star', 'name': 'Sheev Palpatine'}, {'craft': 'ISS', 'name': 'Sally Ride'}, {'craft': 'ISS', 'name': 'Yuri Gagarin'}]}

        self.assertEqual([('Mike', 'Massimino'), ('Sally', 'Ride'), ('Yuri', 'Gagarin')], parse_response(test_response))

    @patch("src.iss_names_service.get_response")
    def test_get_astronaut_names_calls__parse_response_and_get_response(self, mock_get_response):
        mock_get_response.return_value = {'number': 14, 'message': 'success', 'people': [{'craft': 'ISS', 'name': 'Mark Watney'}, {'craft': 'Millenium Falcon', 'name': 'Han Solo'}, {'craft': 'ISS', 'name': 'Paul Atreides'}]}
        expected_return = [('Mark', 'Watney'), ('Paul', 'Atreides')]

        self.assertEqual(expected_return, get_astronaut_names())

    @patch("src.iss_names_service.get_response")
    def test_get_astronaut_names_throws_exception_if_service_unreachable(self, mock_get_response_unreachable):
        mock_get_response_unreachable.side_effect = Exception("service is unreachable")

        self.assertRaisesRegex(Exception, "service is unreachable", get_astronaut_names)

    @patch("src.iss_names_service.get_response")
    def test_get_astronaut_names_throws_exception_if_service_returns_access_error(self, mock_get_response_access_error):
        mock_get_response_access_error.side_effect = Exception("access error")

        self.assertRaisesRegex(Exception, 'access error', get_astronaut_names)  

if __name__ == '__main__':
    unittest.main() 