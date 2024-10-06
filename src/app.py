import logging
import sys

from src.client.image_client import read_image

logger = logging.getLogger("openai_py")
handler = logging.FileHandler("app.log")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def application():
    file_path = "resources/img-1.jpg"
    file = read_image(file_path)
    logger.info(f"File size={sys.getsizeof(file)}")
