import traceback
import os


def requirefolder(foldername: str):
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    elif not os.path.isdir(foldername):
        raise Exception("Requires folder '"+foldername +
                        "', it is however already something else")


def exception_traceback(e):
    return ''.join(traceback.format_exception(None, e, e.__traceback__))


class CustomException(Exception):
    def __init__(self, message, data=None):
        self.message = message
        self.data = data
        super().__init__(self.message)
