import unittest
from unittest.mock import mock_open, patch
from drop_slip import DropSlip, write_drop_slip_to_file

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

    def test_to_text_empty_fields(self):
        course_info = {}

        temp = DropSlip("Ben Johnson", "104023", "Fall 2025", course_info)
        output = temp.to_text()

        self.assertIn("Student Name: Ben Johnson", output)
        self.assertIn("Student ID: 104023", output)
        self.assertIn("CRN:", output)
        self.assertIn("Title:", output)

    @patch("builtins.open", new_callable=mock_open)
    def test_write_drop_slip_to_file(self, mock_file):
        course_info = {
            "crn": "10001",
            "subject": "Math",
            "course_number": "1090",
            "title": "Calculus 2",
            "days": "MWF",
            "time": "10:00-10:50"
        }

        temp = DropSlip("Ben Johnson", "104023", "Fall 2025", course_info)
        filename = write_drop_slip_to_file(temp, "test_output.txt")

        mock_file.assert_called_once_with("test_output.txt", "w", encoding="utf-8")

        handle = mock_file()
        handle.write.assert_called_once_with(temp.to_text())

        self.assertEqual(filename, "test_output.txt")


if __name__ == '__main__':
    unittest.main()