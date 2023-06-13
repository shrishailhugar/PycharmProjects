import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestEx2(BaseClass):
    # Here we are giving dataLoad as a arg bcz dataLoad returning
    def test_login(self,dataLoad):
        log=self.getLogger()
        log.error(dataLoad)
        print(dataLoad[0])
        # itera=iter(dataLoad)
        # print(next(itera))
        # print(next(itera))