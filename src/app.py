import logging
import sys

from src.client.image_client import read_image
from src.client.image_client import find_on_image
from src.client.text_client import text_client

logging.basicConfig(filename='app.log', encoding='UTF-8', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s | %(filename)s | %(message)s')
logger = logging.getLogger(__name__)


def application():
    logger.info('application started')
    response_message = text_client()
    logger.info(f"text_client response_message.content={response_message}")
    # find_on_image("resources/img-1.jpg")
    logger.info('application finished')
