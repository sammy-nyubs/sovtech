from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
import time


class contact_usPagePageObject(PageObject):

    def init_page_elements(self):
        self.legal_consent_checkbx = (By.XPATH, "//input[@id='LEGAL_CONSENT.subscription_type_10841063-c2e387f9-4bd8-496f-ab2a-81fbbc31712a']")
        self.submit_btn = (By.XPATH, "//input[@id='LEGAL_CONSENT.subscription_type_10841063-c2e387f9-4bd8-496f-ab2a-81fbbc31712a']")
        self.get_in_touch = (By.XPATH, "//h2[contains(text(),'Get in touch')]")



    def open(self):
        """ Open contact-us page url in browser

        :returns: this page object instance
        """
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.get_in_touch.wait_until_visible()
        return self

    def fill_get_in_touch_form(self):
        """ Fill the get in touch form and submit

        :returns: this page object instance


        """
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='hs-form-iframe-0']"))
        self.driver.find_element_by_xpath("//input[@id='your_name-c2e387f9-4bd8-496f-ab2a-81fbbc31712a']").send_keys('Sam')
        self.driver.find_element_by_xpath("//input[@id='email-c2e387f9-4bd8-496f-ab2a-81fbbc31712a']").send_keys('Sam@sovtech.com')
        self.driver.find_element_by_xpath("//input[@id='mobilephone-c2e387f9-4bd8-496f-ab2a-81fbbc31712a']").send_keys('0812131311')
        self.driver.find_element_by_xpath("//select[@id='numemployees-c2e387f9-4bd8-496f-ab2a-81fbbc31712a']").click()
        self.driver.find_element_by_xpath("//option[contains(text(),'25-50')]").click()
        self.driver.find_element_by_xpath("//textarea[@id='message-c2e387f9-4bd8-496f-ab2a-81fbbc31712a']").send_keys('Please help me automate the boring stuff!!')
        self.driver.find_element_by_xpath("//input[@id='LEGAL_CONSENT.subscription_type_10841063-c2e387f9-4bd8-496f-ab2a-81fbbc31712a']").click()
        self.driver.find_element_by_xpath("/html/body/div/form/div[7]/div[2]/input").click()
        time.sleep(10)
        return self

