import logging

from openai import OpenAI

logger = logging.getLogger(__name__)


def text_client():
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    )
    response = completion.choices[0]
    logger.info(response)
    return response.message
