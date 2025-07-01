from logger import logging

def add(a,b):
    logging.debug("Addition")
    return a+b

logging.debug("Addition Called")
print(add(10,5))