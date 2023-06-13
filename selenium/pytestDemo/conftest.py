import pytest


# scope=class this will execute once for the class setup before first fun of class teardown (after yield)statements after end of last method from the class

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    # the below lines will be executed after executing all functions
    print("I will be executing last")

#to send data to login
@pytest.fixture()
def dataLoad():
    print("i'm sharing login details")
    return "shree"


#we can send data in tuple format
@pytest.fixture(params=[("user1","password1"),("user2","password2")])
def loginwithCRUD(request):
    print(request.param)
    return request.param