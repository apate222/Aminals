import unittest
import requests

class FlaskTest(unittest.TestCase):

    def test_index(self):
        response = requests.get("http://127.0.0.1:5000/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<h2>Post and view questions that you may be curious about!</h2>' in response.text, True)

    def test_notes(self):
        response = requests.get("http://127.0.0.1:5000/questions")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('Title' and 'Date' in response.text, True)

    def test_note(self):
        response = requests.get("http://127.0.0.1:5000/question/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('First Question' in response.text, True)

    def test_new(self):
        response = requests.get("http://127.0.0.1:5000/questions/new")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<form action="new" method="post">' in response.text, True)

    def test_delete(self):
        response = requests.get('http://127.0.0.1:5000/questions/delete')
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)

    def test_update(self):
        response = requests.get('http://127.0.0.1:5000/questions/edit')
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)

if __name__ == " __main__":
    unittest.main()