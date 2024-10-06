from openai import OpenAI
import sys
import logging
import base64

logger = logging.getLogger(__name__)


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


def parse_answer(response):
    if response.lower() == 'yes':
        return 1
    elif response.lower() == 'no':
        return 0
    else:
        return -1


def find_on_image(image_path):
    logger.debug(f"image_path={image_path}")
    client = OpenAI()

    image = read_image(image_path)
    base64_image = encode_image(image)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Is there a person in a cap on the image? Answer Yes or No"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=1,
    )
    answer = response.choices[0].message.content
    logger.info(f"ChatGPT answer={answer}")
    result = parse_answer(answer)
    print(f"Result={result}")
    return result
