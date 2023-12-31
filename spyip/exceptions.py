"""
All exceptions used in the spyip package
"""


class TooManyRequests(Exception):
    pass


class ConnectionTimeout(Exception):
    pass


class StatusError(Exception):
    pass
