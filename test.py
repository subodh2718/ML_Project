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

# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Calling function:", func.__name__)
#         result = func(*args, **kwargs)
#         print("Function returned:", result)
#         return result
#     return wrapper

# @log_decorator
# def my_function(x, y):
#     return x + y

# my_function(2, 3)

# import matplotlib.pyplot as plt
# import numpy as np

# def spirograph(R, r, d):
#     t = np.linspace(0, 2 * np.pi, 1000)
#     x = (R - r) * np.cos(t) + d * np.cos((R - r) * t / r)
#     y = (R - r) * np.sin(t) - d * np.sin((R - r) * t / r)
#     return x, y

# R = 5
# r = 1
# d = 3

# x, y = spirograph(R, r, d)

# plt.plot(x, y)
# plt.axis("off")
# plt.show()


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

def spirograph(R, r, d):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = (R - r) * np.cos(t) + d * np.cos((R - r) * t / r)
    y = (R - r) * np.sin(t) - d * np.sin((R - r) * t / r)
    return x, y

R = 5
r = 1
d = 3

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x, y = spirograph(R, r, d)
    line.set_data(x[:frame], y[:frame])
    return line,

animation = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Convert each frame of the animation to an image
frames = []
for i in range(100):
    animation._draw_frame(i)
    buf = fig.canvas.tostring_rgb()
    ncols, nrows = fig.canvas.get_width_height()
    img = Image.frombytes("RGB", (ncols, nrows), buf, "raw", "RGB")
    frames.append(img)

# Save the frames as a GIF using Pillow
frames[0].save('spirograph.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)

# Display the GIF in the notebook
from IPython.display import Image
Image(filename='spirograph.gif')

