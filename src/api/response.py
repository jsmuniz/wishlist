from enum import Enum, unique

class Response():
    def __init__(self, status_code, message, data, details):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.details = details
@unique
class ResponseMessages(Enum):
    SUCCESS="The request was successfull"
    ERROR="There were some errors in the request, check details for more information"
    EXCEPTION="An unhandled exception occurred, consult the technical support for more information"