import unittest
from drop_slip import DropSlip

class TestDropSlip(unittest.TestCase):

    def test_to_text(self):
        course_info = {
            "crn": "10001",
            "subject": "Math",
            "course_number": "1090",
            "title": "Calculus 2",
            "days": "MWF",
            "time": "10:00-10:50"
        }

        temp = DropSlip("Ben Johnson", "104023", "Fall 2025", course_info)
        output = temp.to_text()

        self.assertIn("Student Name: Ben Johnson", output)
        self.assertIn("Student ID: 104023", output)
        self.assertIn("CRN: 10001", output)
        self.assertIn("Student Signature:", output)

if __name__ == '__main__':
    unittest.main()