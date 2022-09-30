#Exercise 17.3
import unittest
import modified_python_repos as pr

class StatusCodeTestCase(unittest.TestCase):
    """Test for python_repos.py"""

    def test_status_code(self):
        status_code = pr.r.status_code
        self.assertEqual(status_code, 200)


if __name__ == '__main__':
    unittest.main()        