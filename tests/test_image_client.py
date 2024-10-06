import sys
from unittest import TestCase

from src.client.image_client import read_image, encode_image


class Test(TestCase):
    def test_read_image(self):
        # self.assertRaises(FileNotFoundError, read_image("fake_path_to_image_file"))
        img = read_image("resources/test-img-1.jpg")
        img_base64 = encode_image(img)
        print(f"Image size={sys.getsizeof(img)}")
        print(f"Image Base64 size={sys.getsizeof(img_base64)}")

