import logging
#format
# time:Issue type(Error,warning,Critical,Info): <testcasename> : Description
class BaseClass:

        def getLogger(self):
                # __name__ this is the name of file which will be passed while reporting in order to know from where it's been failed
                #if we not provide __name__  it will print "root"
                logger=logging.getLogger(__name__)


                # here we are using parent -- logging to we need to make connection between fileHandler and logger so that  the logger will get to know which file i need to print
                # we are mentioning the file name inside Filehandler to print logs
                # Now fileHandler is  a object which now have info about where exactly this file is printed
                fileHandler=logging.FileHandler('logfile.log')
                # for the format we need to link
                formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s ")

                #  logger having association with fileHandler so pass Formatter to fileHandler so that logger will get it form fileHandler
                fileHandler.setFormatter(formatter)

                # logger is a object responsible for printing
                logger.addHandler(fileHandler)



                # # print will print in our console in orrder to save logs in file  we need to use logger
                logger.setLevel(logging.DEBUG)
                # logger.debug("A debug statement is printed")
                # logger.info("Information statement")
                # logger.warning("Something wrong")
                # logger.error("A Major error has happened")
                # logger.critical("Critical issue")

                return logger

                #order of printing
                #debug   --- if i set level to info, debug will not print, it will print (info,warning,error,critical) eventhough if we add debug in betwwn those will not print
                #info    --- if we set level to warning it will print all below levels(error ,critical) along with (warning)
                # warning
                # error
                # critica