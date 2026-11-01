import unittest
from datetime import date

from src.main import days_until_exam


class TestDaysUntilExam(unittest.TestCase):
    def test_future_exam(self):
        self.assertEqual(days_until_exam(date(2026, 12, 10), date(2026, 11, 1)), 39)

    def test_exam_today(self):
        self.assertEqual(days_until_exam(date(2026, 11, 1), date(2026, 11, 1)), 0)

    def test_past_exam(self):
        self.assertEqual(days_until_exam(date(2026, 10, 31), date(2026, 11, 1)), -1)


if __name__ == "__main__":
    unittest.main()
