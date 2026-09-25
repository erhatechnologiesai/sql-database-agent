import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestSQLAgent(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_safe_read_query(self):
        res = self.client.post("/query-database", json={"query": "Show customer breakdown by plan"})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data["safety_check_passed"])
        self.assertIn("SELECT", data["generated_sql"])

    def test_forbidden_mutation_blocked(self):
        res = self.client.post("/query-database", json={"query": "DELETE from customers where spend < 100"})
        self.assertEqual(res.status_code, 403)

if __name__ == "__main__":
    unittest.main()
