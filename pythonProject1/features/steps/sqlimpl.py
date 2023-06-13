from behave import given,when,then

from Utilities.Configuration import getqueryparser
from Utilities.Payloadhelper import getsingleentry


@given('SQL {query}')
def step_impl(context,query):
    context.aquery=getqueryparser()[query]
    print(context.aquery)




@when('user asks details of single user')
def step_impl(context):
    entry=getsingleentry(context.aquery)
    print(entry)


@then('it should show customer details')
def step_impl(context):
    pass
