from behave import given, when, then
from pageobjects.contact_us import contact_usPagePageObject


@given('the contact-us page is open')
def step_impl(context):
    context.current_page = contact_usPagePageObject()
    context.current_page.open()


@when('the user navigates to the "Get in touch" section to fill the form')
def step_impl(context):
    context.current_page = contact_usPagePageObject()
    context.current_page.fill_get_in_touch_us_form()


@then('the form fields should be filled and submitted')
def step_impl(context):
    context.current_page = contact_usPagePageObject()
