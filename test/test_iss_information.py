import unittest
from src.iss_information import*

class IssInformationTests(unittest.TestCase):
    
    def test_canary(self):
        self.assertTrue(True)

    def test_get_location_returns_the_time_and_location_that_the_service_returns(self):
        iss_service = lambda: ('11:59PM', 'Houston, TX')

        self.assertEqual(('11:59PM', 'Houston, TX'), get_location(iss_service))

    def test_get_location_returns_string_network_error_if_the_service_throws_exception(self):
        iss_service = lambda: exec('raise(Exception("network error: service unreachable"))')

        self.assertEqual("network error: service unreachable", get_location(iss_service))

    def test_get_location_returns_string_service_failed_to_respond_if_the_service_throws_exception(self):
        iss_service = lambda: exec('raise(Exception("service failed to respond"))')
        
        self.assertEqual("service failed to respond", get_location(iss_service))

    def test_get_astronauts_returns_empty_list_if_service_returns_empty_list(self):
        iss_service = lambda: []

        self.assertEqual([], get_astronauts(iss_service))

    def test_get_astronauts_returns_list_with_one_name_if_service_returns_list_with_one_name(self):
        iss_service = lambda: [('Buzz', 'Aldrin')]

        self.assertEqual([('Buzz', 'Aldrin')], get_astronauts(iss_service))

    def test_get_astronauts_returns_list_with_two_names_if_service_returns_list_with_two_names_already_sorted(self):
        iss_service = lambda: [('Buzz', 'Aldrin'), ('Michael', 'Collins')]

        self.assertEqual([('Buzz', 'Aldrin'), ('Michael', 'Collins')], get_astronauts(iss_service))

    def test_get_astronauts_returns_list_with_two_names_sorted_order_if_service_returns_list_with_two_names_unsorted(self):
        iss_service = lambda: [('Chris', 'Hadfield'), ('Neil', 'Armstrong')]

        self.assertEqual([('Neil', 'Armstrong'), ('Chris', 'Hadfield')], get_astronauts(iss_service))

    def test_get_astronauts_returns_string_network_error_if_service_throws_exception(self):
        iss_service = lambda: exec('raise(Exception("network error: service unreachable"))')

        self.assertEqual("network error: service unreachable", get_astronauts(iss_service))

    def test_get_astronauts_returns_string_service_failed_to_respond_if_the_service_throws_exception(self):
        iss_service = lambda: exec('raise(Exception("service failed to respond"))')
        
        self.assertEqual("service failed to respond", get_astronauts(iss_service))

if __name__ == '__main__':
    unittest.main() 
