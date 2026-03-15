import sys
from src.logger import logging
from flask import logging 

def error_message_details(eroor, error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()     #error_detail.exc_info() returns a tuple of three values: (type, value, traceback)
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in script: [{0}] line number: [{1}] error message: [{2}]".format(
        file_name,exc_tb.tb_lineno,str(eroor)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail)
    def __str__(self):
        return self.error_message
    

    