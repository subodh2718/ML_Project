# import sys

# def divide(x, y):
#     try:
#         result = x / y
#     except:
#         exc_type, exc_value, exc_traceback = sys.exc_info()
#         print(f"Exception: {exc_type}, Value: {exc_value}, Traceback: {exc_traceback}")
#     else:
#         print(f"The result is {result}")

# # Test cases
# divide(4, 2)  # Prints "The result is 2.0"
# divide(4, 0)  # Prints the exception information

## custom Exception

# class NotPalindromeError(Exception):
#     def __init__(self, message):
#         self.message = message

#     def __str__(self):
#         return f"NotPalindromeError: {self.message}"

# def check_palindrome(s):
#     if s != s[::-1]:
#         raise NotPalindromeError(f"{s} is not a palindrome")

# try:
#     check_palindrome("racecar")
#     print("Palindrome!")
#     check_palindrome("hello")
#     print("Palindrome!")
# except NotPalindromeError as e:
#     print(e)


##logger

# import logging

# # create logger object
# logger = logging.getLogger('my_logger')

# # set logging level
# logger.setLevel(logging.DEBUG)

# # create file handler and set level to debug
# fh = logging.FileHandler('debug.log')
# fh.setLevel(logging.WARNING)

# # create console handler and set level to info
# ch = logging.StreamHandler()
# ch.setLevel(logging.WARNING)

# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # add formatter to handlers
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)

# # add handlers to logger
# logger.addHandler(fh)
# logger.addHandler(ch)

# # log some messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')


# import logging
# import logging.handlers
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # create logger object
# logger = logging.getLogger('my_logger')
# logger.setLevel(logging.ERROR)

# # create SMTP handler
# mail_handler = logging.handlers.SMTPHandler(
#     mailhost='smtp.gmail.com',
#     fromaddr='subodh6653@gmail.com',
#     toaddrs=['subodhnigam1@gmail.com'],
#     subject='Error in application',
#     credentials=('subodh6653@gmail.com', 'Infy@6653'),
#     secure=(),
# )

# # set formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# mail_handler.setFormatter(formatter)

# # add handler to logger
# logger.addHandler(mail_handler)

# # log an error message
# try:
#     raise ValueError('This is an example error')
# except ValueError as e:
#     logger.error('An error occurred: %s', e)


##logging and exception

# import logging

# # configure logging
# logging.basicConfig(filename='example.log', level=logging.DEBUG)

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError as e:
#         # handle the exception by logging it
#         logging.error("Error dividing %s by %s: %s", x, y, e)
#     else:
#         # log the result
#         logging.info("Result of dividing %s by %s: %s", x, y, result)
#         return result

# # call the divide function with different arguments
# divide(4, 2)
# divide(4, 0)
# divide("a", 2)


##decorator

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function returned:", result)
        return result
    return wrapper

@log_decorator
def my_function(x, y):
    return x + y

my_function(2, 3)

