Feature: contact-us

  Scenario: navigate to the contact-us page
    Given the contact-us page is open
     When the user navigates to the "Get in touch" section to fill the form
     Then the form fields should be filled and submitted
