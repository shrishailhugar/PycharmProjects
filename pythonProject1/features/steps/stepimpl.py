# from behave import *
# @given('Today is  no Friday')
# def step_impl(context):
#     print("Hi")
#     # raise NotImplementedError(u'STEP: Given Today is  no Friday')
#
#
# @when('user asks today is friday')
# def step_impl(context):
#     print("Here user asked")
#     # raise NotImplementedError('STEP: When user asks today is friday')
#
#
# @then('it should tell today is not friday')
# def step_impl(context):
#     print("Here it's telling today it's  not friday")
#     # raise NotImplementedError(u'STEP: Then it should tell today is not friday')/
#


# from behave import *
# import requests
# from Utilities.Configuration import geturl
#
#
# @given('the {endpoint}')
# def step_impl(context,endpoint):
#     print(geturl())
#     context.endpoint=endpoint
#
# @when('user hit {operation}')
# def step_impl(context,operation):
#     # raise NotImplementedError(u'STEP: When user hit endpoint')
#      response=requests.get(geturl()+context.operation)
#      context.response_code=response.status_code
#      print(response.status_code)
#
#
# @then('user should get {result:d}')
# def step_impl(context,result):
#     assert result==context.response_code
#
#
