import logging

gunicorn_logger = logging.getLogger('gunicorn.debug')

class ConsumerUse:
    """
    Save a new consumer object
    """

    @classmethod
    def receiver(cls, data):
        """
        Write message in logs
        :param data: Example argument
        """
        gunicorn_logger.warning("Message received")
        gunicorn_logger.warning(data)
