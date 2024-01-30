"""
SpyIP Exceptions.
"""


class TooManyRequests(Exception):
    pass


class ConnectionTimeout(Exception):
    pass


class StatusError(Exception):
    pass
