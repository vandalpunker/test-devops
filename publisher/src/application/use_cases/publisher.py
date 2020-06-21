import os
import logging
import requests


class PublisherUse:
    """
    Save a new consumer object
    """

    @classmethod
    def send(cls, message):
        """
        Sends message to url
        :param message: Message to sent
        """
        consumer_url = os.getenv("CONSUMER_URL", None)

        if not consumer_url:
            raise ValueError("CONSUMER_URL env not found")

        response = requests.post(consumer_url, json=message)
        logging.info("Message sent")
        logging.info(response.json())
