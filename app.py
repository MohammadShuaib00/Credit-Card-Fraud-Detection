from creditfraud.logger.logging import logging
from creditfraud.exception.exception import CreditFraudDetection

logging.info("Hello World")
import sys

# Assuming the CreditFraudDetection and error_message_details functions are in 'credit_fraud_detection.py'
# from credit_fraud_detection import CreditFraudDetection

def test_credit_fraud_detection_exception():
    try:
        # Simulating a runtime error
        x = 1 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        # Raise the custom exception with the original error message and details
        raise CreditFraudDetection("A credit fraud detection error occurred.", sys.exc_info())

try:
    test_credit_fraud_detection_exception()
except CreditFraudDetection as e:
    # When the exception is caught, print its string representation, which includes the formatted error message
    print(e)
