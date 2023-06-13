import pytest
import  logging

@pytest.mark.usefixtures("setup")
class Baseclass:
    def getlogger(self):
        logger=logging.getLogger(__name__)
        filehandler=logging.FileHandler("Logfile.log")
        format=logging.Formatter("%(asctime)s : %(levelname)s: %(name)s : %(message)s")
        # format=logging.Formatter("%(asctime)s : %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(format)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
