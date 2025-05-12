import sys
import logger

def error_message_str(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = "Error occured in python script  \n\t name : [{0}] \n\t line number : [{1}] \n\t error_message : [{2}] ".format(file_name,line_number,str(error))
    return error_message


class CustomeException(Exception):
    def __init__(self,error_message , error_details:sys):
        super().__init__(error_message)
        self.error_messsage = error_message_str(error_message,error_details)
    def __str__(self):
        return self.error_messsage
    



if __name__ == "__main__":

    try:
        a = 1/0
    
    except Exception as e:
        logger.logging.info(e)
        raise CustomeException(e,sys)