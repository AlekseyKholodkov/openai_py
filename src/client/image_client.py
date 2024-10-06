from openai import OpenAI
import sys
import logging
import base64

logger = logging.getLogger("image_client")
handler = logging.FileHandler("app.log")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def read_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return image_file.read()
    except FileNotFoundError as e:
        print(f"File '{image_path}' not found!", file=sys.stderr)
        logger.error("File '{image_path}' not found!")
        raise e


def encode_image(image):
    return base64.b64encode(image).decode('utf-8')


def find_on_image():
    client = OpenAI()

    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "What’s in this image?"},
            {
              "type": "image_url",
              "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
              },
            },
          ],
        }
      ],
      max_tokens=300,
    )

    print(response.choices[0])