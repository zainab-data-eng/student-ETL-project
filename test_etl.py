import unittest


def check_result(marks):
    if marks >= 35:
        return "Pass"
    else:
        return "Fail"


class TestETL(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(check_result(85), "Pass")

    def test_fail(self):
        self.assertEqual(check_result(20), "Fail")

    def test_boundary(self):
        self.assertEqual(check_result(35), "Pass")


if __name__ == "__main__":
    unittest.main()
