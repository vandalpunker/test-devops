class ApiException(Exception):
    """
    This is our base Api Exception

    Any Exception in your code must be based with this class
    """

    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        formatted_message = dict(self.payload or ())
        formatted_message["message"] = self.message
        return formatted_message
