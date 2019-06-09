"""The logging module."""

import logging

# TODO make this professional


def info(message: object) -> str:
    """Return log
    :type message: object
    """
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        level=logging.INFO)
    return logging.info(message)


def debug(message: object) -> object:
    """Return log
    :type message: object
    """
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        level=logging.DEBUG)
    return logging.debug(message)


def error(message: object) -> str:
    """Return log
    :type message: object
    """
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        level=logging.ERROR)
    return logging.error(message)
