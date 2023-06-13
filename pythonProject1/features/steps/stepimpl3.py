from behave import *
import requests
from Utilities.Configuration import geturl
from Utilities.Resource import Resource


@given('the {endpoint}')
def step_impl(context,endpoint):
    print(geturl())
    context.endpoint=endpoint

@when('user hit {operation}')
def step_impl(context,operation):
    # raise NotImplementedError(u'STEP: When user hit endpoint')
     print(geturl()+Resource.addbook)
     response=requests.get(geturl()+Resource.addbook)
     context.response_code=response.status_code
     print(response.status_code)


@then('user should get {result:d}')
def step_impl(context,result):
    assert result==context.response_code


