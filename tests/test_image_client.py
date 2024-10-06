import sys
from unittest import TestCase

from src.client.image_client import read_image, encode_image, parse_answer


class Test(TestCase):
    def test_read_image(self):
        # self.assertRaises(FileNotFoundError, read_image("fake_path_to_image_file"))
        img = read_image("resources/test-img-1.jpg")
        img_base64 = encode_image(img)
        print(f"Image size={sys.getsizeof(img)}")
        print(f"Image Base64 size={sys.getsizeof(img_base64)}")

    def test_parse_answer(self):
        self.assertEqual(1, parse_answer("Yes"))
        self.assertEqual(1, parse_answer("YES"))
        self.assertEqual(1, parse_answer("yEs"))
        self.assertEqual(1, parse_answer("yes"))
        self.assertEqual(0, parse_answer("NO"))
        self.assertEqual(0, parse_answer("no"))
        self.assertEqual(0, parse_answer("No"))
        self.assertEqual(0, parse_answer("nO"))
        self.assertEqual(-1, parse_answer("Unknown"))
        self.assertEqual(-1, parse_answer("any unexpected answer"))

