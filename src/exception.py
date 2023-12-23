import sys
sys.path.append('/Users/Vaibhav.Mittal/Assignments/ML_Project')
from src.logger import logging

def error_messsage_details(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error_message[{2}]".format(
        file_name, exc_tb.tb_lineno,str(error)
        )
    return error_message

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_messsage_details(error_message, error_detail=error_detail)
        logging.info(self.error_message)
    def __str__(self):
        return self.error_message


# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as err:
#         raise CustomException(err, sys)