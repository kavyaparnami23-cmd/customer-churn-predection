import sys


def error_message_detail(error: Exception, error_detail: sys):

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = (
        f"\nError occurred in Python Script: [{file_name}]"
        f"\nLine Number: [{exc_tb.tb_lineno}]"
        f"\nError Message: [{str(error)}]"
    )

    return error_message


class CustomException(Exception):
    """
    Custom Exception Class
    """

    def __init__(self, error_message: Exception, error_detail: sys):

        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message,
            error_detail
        )

    def __str__(self):

        return self.error_message


if __name__ == "__main__":

    try:

        a = 10 / 0

    except Exception as e:

        raise CustomException(e, sys)