#ANY PYTEST FIle should sbe prefixed  with test_ or end wih _test
#pytest method names should be prefixed with _test
#any code should be wrapped with methods
#in pytest don't write 2 methods with same name else the last defined function overrides the first function
#method names should have sense so that we can run function
import pytest


#to execute but not report when it's results are dependent for another testcase but it' failing at that time we can run that method but not going to show in reporting
@pytest.mark.xfail
def test_firstProgram():
    a=1
    assert a==2 ,"a is not matching"

@pytest.mark.smoke
@pytest.mark.skip
def test_secondProgram():
    print("Good Morning GURU")

def test_secondProgram1():
    print("Good Morning BAPU")