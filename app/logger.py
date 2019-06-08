"""Extensions module - Set up for additional libraries can go in here."""
import logging


def log(message: object) -> str:
    """Return log
    :type message: object
    """
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        level=logging.INFO)
    return logging.info(message)
