# WST defined Exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ZeroResultException(Error):
    """Zero result exception"""
    pass


class UnknownCondition(Error):
    """If an unknown, unexisted conditions comes from the frontend."""
    pass


class UnknownLogic(Error):
    """If an unknown logic comes from the web"""
    pass


class UnknownEntry(Error):
    """If an unknown entry comes from the web"""
    pass


class UnknownOrder(Error):
    """If an unknown order comes from the web"""
    pass


class LogicalWasNotGiven(Error):
    """If 2 or more filtered sent but at minimum one logic condition is missing"""
    pass


class TooManyPages(Error):
    """If an unexisting page wanted to be shown"""
    pass
