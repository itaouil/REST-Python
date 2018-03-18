import sys
import json
import unittest
import flaskapi
import requests

class TestFlaskApiUsingRequests(unittest.TestCase):

    def test_add(self):
        response = requests.post('http://localhost:5000/add', json={'name': 'test',
                                                                    'species': 'test',
                                                                    'gender': 'm',
                                                                    'birthday': 1111111111})
        self.assertEqual(response.json(), {'success': 'True'})

    def test_update(self):
        response = requests.post('http://localhost:5000/add', json={'id': 10,
                                                                    'name': 'test',
                                                                    'species': 'test',
                                                                    'gender': 'm',
                                                                    'birthday': 1111111111})
        self.assertEqual(response.json(), {'success': 'True'})

    # TODO: Test invalidity for add endpoint

    # TODO: Test invalidity for update endpoint

    # TODO: Test invalidity for list endpoint

if __name__ == "__main__":
    unittest.main()
