import logging
import os
import sys
from datetime import datetime
import traceback

def error_message_details(error, error_detail):
    """
    Generates a detailed error message with traceback information.

    Args:
        error (Exception): The exception that was raised.
        error_detail (tuple): The details of the exception, typically provided by sys.exc_info().
    
    Returns:
        str: A formatted string containing the file name, line number, error message, and the traceback details.
    """
    exc_type, exc_value, exc_tb = error_detail
    
    # Check if traceback is available
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return (
            f"Error occurred in script {file_name}, "
            f"line number {line_number}, "
            f"error message: {str(error)}, "
            f"traceback: {''.join(traceback.format_exception(exc_type, exc_value, exc_tb))}"
        )
    else:
        return f"Error occurred: {str(error)}"

class CreditFraudDetection(Exception):
    """
    Custom exception for credit fraud detection with detailed error message and traceback.

    Args:
        error_message (str): The error message to be raised.
        error_details (tuple, optional): The error details, typically provided by sys.exc_info(). Defaults to None.
    
    Attributes:
        error_message (str): The formatted error message with traceback details.
    
    Methods:
        __str__(): Returns the error message with traceback information.
    """
    def __init__(self, error_message, error_details=None):
        """
        Initializes the exception with a custom error message and traceback details.

        Args:
            error_message (str): The error message to be raised.
            error_details (tuple, optional): The error details, typically provided by sys.exc_info(). Defaults to None.
        """
        if error_details is None:
            error_details = sys.exc_info()
        super().__init__(error_message)  # Initialize base class with error_message
        self.error_message = error_message_details(error_message, error_details)  # Capture the detailed error message

    def __str__(self):
        """
        Returns the formatted error message with traceback information.

        Returns:
            str: The error message containing details about the exception and traceback.
        """
        return self.error_message
