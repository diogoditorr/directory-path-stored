class Error(Exception):
    pass

class OverwriteError(Error):
    """Exception raised when the user tries to overwrite an existing directory shortcut."""
    pass
