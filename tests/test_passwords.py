import unittest
from services.password_service import PasswordService

class TestPassword(unittest.TestCase):

    def test_length(self):
        service = PasswordService()
        pwd = service.generate_password(10)
        self.assertEqual(len(pwd), 10)

    def test_not_empty(self):
        service = PasswordService()
        pwd = service.generate_password()
        self.assertTrue(len(pwd) > 0)

if __name__ == "__main__":
    unittest.main()



