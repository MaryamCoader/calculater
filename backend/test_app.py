import unittest
import json
from app import app  # Assuming your Flask app is in app.py

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"status": "ok"})

    def test_add_operation(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "add", "a": 5, "b": 3}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"result": 8, "error": None})

    def test_subtract_operation(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "subtract", "a": 10, "b": 4}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"result": 6, "error": None})

    def test_multiply_operation(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "multiply", "a": 6, "b": 7}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"result": 42, "error": None})

    def test_divide_operation(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "divide", "a": 10, "b": 2}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"result": 5, "error": None})

    def test_divide_by_zero(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "divide", "a": 10, "b": 0}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"result": None, "error": "Division by zero is not allowed"})

    def test_modulo_operation(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "modulo", "a": 10, "b": 3}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"result": 1, "error": None})

    def test_power_operation(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "power", "a": 2, "b": 3}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"result": 8, "error": None})

    def test_missing_parameters(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "add", "a": 5}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"result": None, "error": "Missing 'op', 'a', or 'b' parameters"})

    def test_invalid_numbers(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "add", "a": "five", "b": 3}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"result": None, "error": "Parameters 'a' and 'b' must be numbers"})

    def test_unsupported_operation(self):
        response = self.app.post('/api/calc',
                                 data=json.dumps({"op": "unsupported", "a": 1, "b": 2}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"result": None, "error": "Unsupported operation: unsupported"})

if __name__ == '__main__':
    unittest.main()
